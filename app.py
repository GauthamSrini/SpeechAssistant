from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    r = sr.Recognizer()
    text = ""

    if 'use_microphone' in request.form:
        audio = r.listen(sr.Microphone())
        text = recognize_speech(r, audio)

    if text:
        return render_template('index.html', text=text)
    else:
        error = "No speech input detected."
        return render_template('index.html', error=error)

def recognize_speech(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
