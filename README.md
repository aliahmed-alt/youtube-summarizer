# YouTube Summarizer

A simple Flask web application that allows users to input a YouTube video URL, download the video's audio, transcribe it using OpenAI's Whisper model, and generate a summary of the transcribed text.

## Features

- **Input YouTube Video URL**: Users can input the URL of a YouTube video.
- **Audio Downloading**: Downloads the audio from the YouTube video.
- **Transcription**: Transcribes the downloaded audio using the Whisper model.
- **Summarization**: Generates a summary of the transcribed text.
- **User-friendly Interface**: A web-based interface for easy interaction.

## Technologies Used

- **Flask**: For creating the web application.
- **Whisper**: OpenAI's speech-to-text model used for transcription.
- **yt-dlp**: A video downloader for extracting audio from YouTube.
- **HTML/CSS/JavaScript**: For creating the frontend user interface.
- **Bootstrap**: Used for styling and responsive design.
  
## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/aliahmed-alt/youtube-summarizer.git
   cd youtube-summarizer
Set up a virtual environment (optional but recommended):

bash


python -m venv venv
source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
Install required dependencies:

bash


pip install -r requirements.txt
Run the application:

bash


python app.py
This will start a development server. You can visit http://127.0.0.1:5000/ in your browser to access the application.

Usage
Visit the Website: Open the Flask application in your browser.

Paste a YouTube Video URL: Enter the URL of the YouTube video you want to summarize.

Click "Summarize": After the video is processed, you will see the summary of the transcription.

Project Structure
php


youtube-summarizer/
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── static/               # Contains CSS, JS, and images
│   └── loading.gif       # Loading animation
│
├── templates/            # Contains HTML templates
│   └── index.html        # Main webpage template
├── yt-dlp.log            # Log file for debugging yt-dlp
└── README.md             # Project README file
Contributing
If you'd like to contribute to this project, feel free to fork the repository, make changes, and create a pull request. Your contributions are welcome!

License
This project is open-source and available under the MIT License.

Developer
GitBejgo: Developer and creator of the YouTube Summarizer tool.

Acknowledgments
OpenAI Whisper: For the transcription capabilities.

yt-dlp: For downloading audio from YouTube.

Flask: For the web framework.

Bootstrap: For responsive design.

markdown



### Key Sections:
- **Project Features**: Lists the main features and what the application does.
- **Technologies Used**: Details the libraries and tools used in the project.
- **Installation**: How to set up the project locally.
- **Usage**: How to use the app after setup.
- **Project Structure**: Provides a brief explanation of the folder and file structure.
- **Contributing**: Encourages others to contribute to the project.
- **Developer**: Credits you as the developer (GitBejgo).
- **License**: Includes a placeholder for the MIT License.
