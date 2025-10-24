import os
import time
import requests
from dotenv import load_dotenv

# =========================
# CONFIGURAÇÃO TELEGRAM
# =========================
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# =========================
# FUNÇÃO PARA ENVIAR MENSAGEM
# =========================
def enviar_mensagem_telegram(texto):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": texto, "parse_mode": "HTML"}
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print("✅ Mensagem enviada ao Telegram!")
        else:
            print(f"⚠️ Falha ao enviar mensagem ({response.text})")
    except Exception as e:
        print(f"❌ Erro ao conectar ao Telegram: {e}")

# =========================
# FUNÇÃO PRINCIPAL DO BOT
# =========================
def main():
    print("🚀 Bot Basejump iniciado!")
    enviar_mensagem_telegram("🤖 Bot Basejump iniciado com sucesso!")

    # Aqui você pode rodar seu script de automação Selenium ou agendar execuções diárias
    while True:
        # Exemplo: envia mensagem de status a cada 24h
        enviar_mensagem_telegram("📊 Execução automática completa — tudo funcionando!")
        print("🕐 Aguardando próxima execução...")
        time.sleep(86400)  # 24h = 86400 segundos

if __name__ == "__main__":
    main()
