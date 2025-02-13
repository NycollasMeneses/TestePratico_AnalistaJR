from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

USERS_DB = {
    "admin": "pbkdf2:sha256:260000$Y9LirPL3$..."
}

@app.route('/login', methods=['POST'])
@limiter.limit("5 per minute")  # Limite de tentativas
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in USERS_DB and check_password_hash(USERS_DB[username], password):
        return jsonify({"message": "Acesso concedido"}), 200

    return jsonify({"message": "Acesso negado"}), 401

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)