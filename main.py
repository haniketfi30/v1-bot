import requests
from bs4 import BeautifulSoup
import time
from flask import Flask
from threading import Thread
import os

# --- 1. كود Flask لإبقاء البوت حياً على Render ---
app = Flask('')

@app.route('/')
def home():
    return "V1_ESPORT Bot is Running!"

def run():
    # Render يستخدم Port ديناميكي، هذا السطر يقرأه تلقائياً
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()

# --- 2. إعدادات بوت V1_ESPORT ---
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1344243640003002388/m5V4qY-kP-Xf7G0O0u0-0u0-0u0" # تأكد من رابط الويهبوك الخاص بك
RSS_URL = "https://rss.app/feeds/c3qBqY8m5N0v7S6L" # رابط التغذية الخاص بالبطولات

seen_links = set()

def check_tournaments():
    try:
        print("🔎 v1_esport: Checking for new tournaments...")
        response = requests.get(RSS_URL)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')

        for item in items:
            title = item.title.text
            link = item.link.text
            
            if link not in seen_links:
                # إرسال إشعار لديسكورد
                payload = {
                    "content": f"📢 **بطولة جديدة مكتشفة!**\n🏆 {title}\n🔗 {link}"
                }
                requests.post(DISCORD_WEBHOOK, json=payload)
                seen_links.add(link)
                print(f"✅ Sent: {title}")

    except Exception as e:
        print(f"❌ Error: {e}")

# --- 3. تشغيل كل شيء معاً ---
if __name__ == "__main__":
    # تشغيل السيرفر الوهمي في الخلفية
    keep_alive()
    
    # حلقة تشغيل البوت الأساسية
    while True:
        check_tournaments()
        # يفحص كل 10 دقائق (600 ثانية)
        time.sleep(600)
