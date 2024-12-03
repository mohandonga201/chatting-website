from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return jsonify({'message': 'Chat backend is running!'})

@socketio.on('message')
def handle_message(message):
    print(f"Received message: {message}")
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)

