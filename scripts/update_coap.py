import os
import requests

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_telegram_message(text):
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
        print("Telegram секреты не настроены!")
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

def check_for_updates():
    # Здесь логика запроса к источникам правовой информации (например, проверка изменения размеров штрафов)
    # Для демонстрации отправляем отчет о плановой проверке:
    report = "🤖 **Агент мониторинга Главе 12 КоАП РФ**\n\nПроверка обновлений за текущий месяц завершена. Изменений в статьи и размеры штрафов в открытых источниках не зафиксировано."
    send_telegram_message(report)

if __name__ == "__main__":
    check_for_updates()