from flask import Flask
from threading import Thread
import requests
import time
import os

app = Flask(__name__)

# ضع رابط الويب هوك الخاص بك هنا
DISCORD_WEBHOOK_URL = "ضع_رابط_الويب_هوك_هنا"
TARGET_URL = "https://www.challengermode.com/fortnite/tournaments"

@app.route('/')
def home():
    return "V1 Bot is running 24/7!"

def track_tournaments():
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": "🚀 **V1 Tracker** اشتغل بنجاح وهو الآن يعمل على السيرفر!"})
    except:
        pass

    while True:
        try:
            response = requests.get(TARGET_URL, timeout=15)
            if response.status_code == 200:
                print("Server checked successfully.")
            # يفحص كل 10 دقائق
            time.sleep(600)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(60)

def keep_alive():
    t = Thread(target=track_tournaments)
    t.start()

if __name__ == "__main__":
    keep_alive()
    # هذا السطر هو الذي سيحل مشكلة الـ Port في Render
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
