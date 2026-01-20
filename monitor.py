import requests
import os
import re

NEWS_URL = "https://travel.state.gov/content/travel/en/News/visas-news.html"
DV_URL = "https://dvprogram.state.gov/"

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": True
        }
    )

def get_latest_news(html: str):
    match = re.search(
        r'([A-Z][a-z]{2} \d{1,2}, \d{4}).*?href="([^"]+)".*?>([^<]+)</a>',
        html,
        re.S
    )
    if not match:
        return None

    date, link, title = match.groups()
    return f"{date} | {title.strip()}"

html = requests.get(NEWS_URL, timeout=20).text
latest = get_latest_news(html)

if not latest:
    exit(0)

try:
    with open("last_news.txt", "r", encoding="utf-8") as f:
        old = f.read().strip()
except FileNotFoundError:
    old = ""

if latest != old:
    send("🚨 NEW U.S. VISA NEWS UPDATE")
    send(latest)
    send(f"Check DV Lottery page:\n{DV_URL}")

    with open("last_news.txt", "w", encoding="utf-8") as f:
        f.write(latest)
