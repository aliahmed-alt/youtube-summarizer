from flask import Flask, request, jsonify, render_template
import whisper
import os
import yt_dlp as youtube_dl
import logging
from transformers import pipeline

app = Flask(__name__)

# Ensure a folder for downloads exists
DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# Set up logging for verbose output
logging.basicConfig(filename='yt-dlp.log', level=logging.DEBUG)

# Load the summarization model from Hugging Face
summarizer = pipeline("summarization")

# Function to split text into smaller chunks
def chunk_text(text, max_length=1024):
    words = text.split()
    chunks = []
    chunk = []

    for word in words:
        chunk.append(word)
        if len(" ".join(chunk)) > max_length:
            chunks.append(" ".join(chunk[:-1]))
            chunk = [word]

    if chunk:
        chunks.append(" ".join(chunk))
    
    return chunks

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    video_url = data.get('video_url')

    if not video_url:
        return jsonify({'error': 'No video URL provided'}), 400

    try:
        # Download audio from YouTube
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
            'verbose': True  # Enable verbose mode
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            audio_path = os.path.join(DOWNLOAD_FOLDER, f"{info['id']}.mp3")

        # Check if the file is downloaded
        if not os.path.exists(audio_path):
            raise Exception("Audio file not downloaded successfully.")

        # Load Whisper model and transcribe
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        transcript = result['text']

        # Chunk the transcript if it's too long
        chunks = chunk_text(transcript)

        # Summarize each chunk and combine the results
        summaries = []
        for chunk in chunks:
            summary = summarizer(chunk, max_length=200, min_length=50, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        # Combine the summarized chunks
        full_summary = " ".join(summaries)

        return jsonify({'summary': full_summary})

    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
