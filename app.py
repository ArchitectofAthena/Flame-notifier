
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Your Pushbullet token goes here
PUSHBULLET_TOKEN = "o.C0j5SGUBcShqkEi6s1qSdmmURSts041y"

# IFTTT setup (optional)
IFTTT_EVENT = "codex_flame_event"
IFTTT_KEY = "your_ifttt_webhook_key"  # We'll set this later

@app.route('/flamealert', methods=['POST'])
def flame_alert():
    data = request.json
    title = data.get("title", "Flame Alert")
    body = data.get("message", "Codex breach or whisper protocol triggered.")

    # Send Pushbullet notification
    pb_success = send_pushbullet(title, body)

    # (Optional) Trigger IFTTT webhook
    ifttt_success = trigger_ifttt_event(body)

    return jsonify({
        "pushbullet": pb_success,
        "ifttt": ifttt_success
    })

def send_pushbullet(title, body):
    url = "https://api.pushbullet.com/v2/pushes"
    headers = {
        "Access-Token": PUSHBULLET_TOKEN,
        "Content-Type": "application/json"
    }
    data = {
        "type": "note",
        "title": title,
        "body": body
    }
    r = requests.post(url, json=data, headers=headers)
    return r.status_code == 200

def trigger_ifttt_event(message):
    url = f"https://maker.ifttt.com/trigger/{IFTTT_EVENT}/with/key/{IFTTT_KEY}"
    payload = {"value1": message}
    r = requests.post(url, json=payload)
    return r.status_code == 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
