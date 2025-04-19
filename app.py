
from flask import Flask, request
import pyttsx3
import os

app = Flask(__name__)
engine = pyttsx3.init()

@app.route('/')
def home():
    return "Flame Notifier is live and ready, baby!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text", "")
    if text:
        engine.say(text)
        engine.runAndWait()
        return {"status": f"Speaking: {text}"}
    return {"error": "No text provided"}, 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)