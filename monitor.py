import requests, hashlib, os

URL = "https://dvprogram.state.gov/"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": text}
    )

r = requests.get(URL, timeout=20)
h = hashlib.md5(r.text.encode()).hexdigest()

try:
    old = open("hash.txt").read()
except:
    old = ""

if h != old:
    send("🚨 DV Lottery site updated! https://dvprogram.state.gov/")
    open("hash.txt","w").write(h)
