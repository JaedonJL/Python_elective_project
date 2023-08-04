import requests

def send_telegram_message(bot_token, chat_id, message):
    base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": message,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")

# Replace 'YOUR_BOT_TOKEN' with the actual API token of your Telegram bot
bot_token = '6584510597:AAHe3yzXCntJJbuyjFrihapke83QtXl_LLc'

# Replace 'YOUR_CHAT_ID' with the chat ID of the user or group you want to send messages to
chat_id = 'YOUR_CHAT_ID'

# The message you want to send
message = "Hello, this is a message from your Telegram bot!"

send_telegram_message(bot_token, chat_id, message)