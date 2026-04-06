import requests
import time

# ضع رابط الويب هوك الذي نسخته هنا بين القوسين
DISCORD_WEBHOOK_URL = "رابط_الويب_هوك_الخاص_بك_هنا"

# الرابط المراد مراقبته (Challengermode)
TARGET_URL = "https://www.challengermode.com/fortnite/tournaments"

def send_to_discord(message):
    try:
        data = {"content": message}
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Error sending to Discord: {e}")

if __name__ == "__main__":
    print("V1 Tracker is starting...")
    # إرسال رسالة تجريبية فور تشغيل البوت للتأكد من الاتصال
    send_to_discord("🚀 V1 Tracker is now LIVE and monitoring Challengermode!")
    
    while True:
        try:
            # هنا تتم عملية الفحص (بسيطة حالياً للتأكد من عمل السيرفر)
            response = requests.get(TARGET_URL, timeout=10)
            if response.status_code == 200:
                print("Check successful, server is responding.")
            
            # انتظر 10 دقائق قبل الفحص التالي
            time.sleep(600)
        except Exception as e:
            print(f"Loop error: {e}")
            time.sleep(60)
