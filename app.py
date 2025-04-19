
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flame Notifier is live and ready, baby!"

# Required for Render deployment: bind to 0.0.0.0 and use the PORT environment variable
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
