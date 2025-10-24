import os
import requests
from flask import Flask, request

TOKEN = os.getenv("TELEGRAM_TOKEN", "8222228238:AAFyzX1rnDrN9wfVdjYLB6fU9fyyPkl2RoU")

app = Flask(__name__)

# =========================
# ROTA RAIZ (teste)
# =========================
@app.route("/", methods=["GET"])
def home():
    return "✅ Bot Basejump Telegram está online!", 200


# =========================
# ROTA DO TELEGRAM WEBHOOK
# =========================
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)
        print(f"📩 Recebido update: {data}")

        if "message" not in data:
            print("⚠️ Nenhuma mensagem encontrada no update.")
            return "no message", 200

        chat_id = data["message"]["chat"]["id"]
        nome = data["message"]["from"].get("first_name", "Usuário")
        texto = data["message"].get("text", "").lower()

        if "oi" in texto or "id" in texto or "/start" in texto:
            resposta = f"👋 Olá, {nome}! Seu <b>chat_id</b> é: <code>{chat_id}</code>"
        else:
            resposta = "🤖 Envie 'oi' ou 'id' para descobrir seu chat_id."

        enviar_mensagem(chat_id, resposta)
        return "ok", 200

    except Exception as e:
        print(f"❌ Erro ao processar webhook: {e}")
        return "error", 500


# =========================
# FUNÇÃO PARA ENVIAR MENSAGEM
# =========================
def enviar_mensagem(chat_id, texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "HTML"
    }
    try:
        resp = requests.post(url, json=payload)
        print(f"📤 Mensagem enviada para {chat_id}: {resp.status_code}")
    except Exception as e:
        print(f"⚠️ Falha ao enviar mensagem: {e}")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))  # Render usa porta 10000
    print(f"🚀 Bot Basejump rodando na porta {port}")
    app.run(host="0.0.0.0", port=port)
