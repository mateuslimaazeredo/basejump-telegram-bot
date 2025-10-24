import os
import requests
from flask import Flask, request
from dotenv import load_dotenv

# =========================
# CONFIGURAÇÃO
# =========================
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

app = Flask(__name__)

# =========================
# ROTA PARA RECEBER MENSAGENS
# =========================
@app.route(f"/{TOKEN}", methods=["POST"])
def responder():
    try:
        data = request.get_json()
        chat_id = data["message"]["chat"]["id"]
        nome = data["message"]["from"].get("first_name", "Usuário")
        texto = data["message"].get("text", "").lower()

        print(f"📩 Mensagem recebida de {nome} ({chat_id}): {texto}")

        if "oi" in texto or "id" in texto:
            resposta = f"👋 Olá, {nome}! Seu <b>chat_id</b> é: <code>{chat_id}</code>"
        else:
            resposta = f"🤖 Oi, {nome}! Envie 'ID' para descobrir seu chat_id."

        # Envia resposta
        requests.post(
            f"https://api.telegram.org/bot{TOKEN}/sendMessage",
            json={
                "chat_id": chat_id,
                "text": resposta,
                "parse_mode": "HTML"
            }
        )

        return "ok", 200

    except Exception as e:
        print(f"⚠️ Erro ao processar mensagem: {e}")
        return "error", 500


# =========================
# ROTA PRINCIPAL (para o Render manter vivo)
# =========================
@app.route("/")
def home():
    return "✅ Bot Basejump Telegram está online!", 200


# =========================
# FUNÇÃO PRINCIPAL
# =========================
if __name__ == "__main__":
    print("🚀 Bot Basejump iniciado!")
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
