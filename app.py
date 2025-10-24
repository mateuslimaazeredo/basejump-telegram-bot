import os
import requests
from flask import Flask, request

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")

@app.route(f"/{TOKEN}", methods=["POST"])
def responder():
    data = request.get_json()
    chat_id = data["message"]["chat"]["id"]
    texto = data["message"]["text"]

    resposta = f"👋 Olá! Seu chat_id é: <b>{chat_id}</b>"
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        json={"chat_id": chat_id, "text": resposta, "parse_mode": "HTML"}
    )
    return "ok"

@app.route("/")
def home():
    return "Bot Basejump ativo!"

if __name__ == "__main__":
    app.run(port=5000)
