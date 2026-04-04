import requests
from bs4 import BeautifulSoup
import time

# إعدادات v1_esport
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1489623638645932153/mgi5XdBejwEbiexRMmwnUecJ6B9peBOsB2D-nUturmkW3zwTh3IE-XtL10_arRI5RdbW"
RSS_URL = "https://rss.app/feeds/c3qBN0KG9Xc20Zf9.xml"

# لمنع التكرار
seen_links = set()

def check_tournaments():
    try:
        print("🔎 v1_esport: Checking for new tournaments...")
        response = requests.get(RSS_URL, timeout=10)
        soup = BeautifulSoup(response.content, 'xml')
        items = soup.find_all('item')
        
        for item in items:
            link = item.link.text
            title = item.title.text
            
            if link not in seen_links:
                print(f"✅ Found: {title}")
                payload = {
                    "content": f"🦅 **تنبيه v1_esport: بطولة جديدة!**\n\n📌 {title}\n🔗 {link}"
                }
                requests.post(DISCORD_WEBHOOK, json=payload)
                seen_links.add(link)
    except Exception as e:
        print(f"❌ Error: {e}")

# فحص كل 5 دقائق
while True:
    check_tournaments()
    time.sleep(300)

