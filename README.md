
# Speech Recognizer
This project is a Speech-to-Text (STT) Converter built with Flask. It provides a web-based interface where users can upload audio files or use their microphone to convert speech into text. The goal is to enable efficient and accurate speech-to-text conversion for a variety of applications such as note-taking, transcription, and more.



## Features
- Audio File Upload: Upload .wav, .flac, or .mp3 files for speech-to-text conversion.
- Live Microphone Input: Use your device's microphone to transcribe live speech.
- Error Handling: Displays appropriate error messages if speech is not detected or other issues arise.
- Downloadable Results: Provides the option to download the transcribed text.
## Installation

Install the required packages

```bash
  pip install -r requirements.txt
```
This will install 

- Flask==2.1.0
- SpeechRecognition==3.8.1
- Gunicorn==20.1.0
## Running the Application

To start the Flask application, use the following command:

```bash
  python app.py

```


## Usage

- Upload Audio File: Select an audio file from your computer (supported formats: .wav, .flac, .mp3).
- Convert Speech to Text: Click "Convert" to transcribe the audio into text.
- Use Microphone: Click the "Use Microphone" button to start capturing live speech.
- Download Output: After the conversion, the transcribed text will be displayed, with options to download the output.


## Technologies Used

- Flask: A micro web framework for Python.
- SpeechRecognition: Python library for performing speech recognition via Google Speech API.
- HTML/CSS: Used for the frontend layout and design.
- Gunicorn: WSGI HTTP Server for running the app in production.

