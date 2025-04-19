from flask import Flask, request
from flask_cors import CORS
import pyttsx3
import logging
import os

app = Flask(__name__)
CORS(app)  # Allow external access, useful for frontend use

# Logging config
logging.basicConfig(level=logging.INFO)

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)      # Adjust speaking speed
engine.setProperty('volume', 1.0)    # Volume range: 0.0 to 1.0
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose a voice (0 = default)

@app.route('/')
def home():
    return 'Flame Notifier is live and ready, baby!'

@app.route('/speak', methods=['POST'])
def speak():
    data = request.get_json()
    if not data or 'text' not in data:
        return 'Missing "text" in JSON.', 400

    text = data['text']
    logging.info(f"Received text: {text}")

    try:
        engine.say(text)
        engine.runAndWait()
        logging.info(f"Spoken text: {text}")
        return f'Spoken: "{text}"'
    except Exception as e:
        logging.error(f"Speech error: {e}")
        return f"Error: {str(e)}", 500

# Render deployment setup
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)