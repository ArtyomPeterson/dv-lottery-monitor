import requests
import difflib
import os
import re

URL = "https://dvprogram.state.gov/"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

IMPORTANT_KEYWORDS = [
    "entry period",
    "is now open",
    "dv-202",
    "check status",
    "submit",
]

def send(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": True
        }
    )

def clean_html(html: str) -> str:
    # remove scripts, styles, meta, noscript
    html = re.sub(r"<script.*?>.*?</script>", "", html, flags=re.S)
    html = re.sub(r"<style.*?>.*?</style>", "", html, flags=re.S)
    html = re.sub(r"<meta.*?>", "", html, flags=re.S)
    html = re.sub(r"<noscript.*?>.*?</noscript>", "", html, flags=re.S)
    # remove all tags
    html = re.sub(r"<[^>]+>", "", html)
    # normalize whitespace
    html = re.sub(r"\s+", " ", html)
    return html.strip()

# 1. Download page
response = requests.get(URL, timeout=20)
cleaned_new = clean_html(response.text)
new_lines = cleaned_new.splitlines()

# 2. Load previous version
try:
    with open("page_old.txt", "r", encoding="utf-8") as f:
        old_lines = f.read().splitlines()
except FileNotFoundError:
    old_lines = []

# 3. Check important keywords
lower_text = cleaned_new.lower()
important_hits = [
    kw for kw in IMPORTANT_KEYWORDS if kw in lower_text
]

# 4. Diff
diff = list(difflib.unified_diff(
    old_lines,
    new_lines,
    fromfile="before",
    tofile="after",
    lineterm=""
))

# 5. React
if diff:
    diff_text = "\n".join(diff[:80])

    if important_hits:
        send(
            "🚨🚨 IMPORTANT DV LOTTERY UPDATE 🚨🚨\n\n"
            f"Keywords detected: {', '.join(important_hits)}\n\n"
            "⚠️ CHECK THE SITE IMMEDIATELY:\n"
            "https://dvprogram.state.gov/"
        )

    send(
        "ℹ️ DV Lottery site changed.\n\n"
        "🔍 Diff (cleaned text):\n"
        "```\n"
        f"{diff_text}\n"
        "```"
    )

    with open("page_old.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
import requests
import difflib
import os
import re

URL = "https://dvprogram.state.gov/"
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

IMPORTANT_KEYWORDS = [
    "entry period",
    "is now open",
    "dv-202",
    "check status",
    "submit",
]

def send(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text,
            "disable_web_page_preview": True
        }
    )

def clean_html(html: str) -> str:
    # remove scripts, styles, meta, noscript
    html = re.sub(r"<script.*?>.*?</script>", "", html, flags=re.S)
    html = re.sub(r"<style.*?>.*?</style>", "", html, flags=re.S)
    html = re.sub(r"<meta.*?>", "", html, flags=re.S)
    html = re.sub(r"<noscript.*?>.*?</noscript>", "", html, flags=re.S)
    # remove all tags
    html = re.sub(r"<[^>]+>", "", html)
    # normalize whitespace
    html = re.sub(r"\s+", " ", html)
    return html.strip()

# 1. Download page
response = requests.get(URL, timeout=20)
cleaned_new = clean_html(response.text)
new_lines = cleaned_new.splitlines()

# 2. Load previous version
try:
    with open("page_old.txt", "r", encoding="utf-8") as f:
        old_lines = f.read().splitlines()
except FileNotFoundError:
    old_lines = []

# 3. Check important keywords
lower_text = cleaned_new.lower()
important_hits = [
    kw for kw in IMPORTANT_KEYWORDS if kw in lower_text
]

# 4. Diff
diff = list(difflib.unified_diff(
    old_lines,
    new_lines,
    fromfile="before",
    tofile="after",
    lineterm=""
))

# 5. React
if diff:
    diff_text = "\n".join(diff[:80])

    if important_hits:
        send(
            "🚨🚨 IMPORTANT DV LOTTERY UPDATE 🚨🚨\n\n"
            f"Keywords detected: {', '.join(important_hits)}\n\n"
            "⚠️ CHECK THE SITE IMMEDIATELY:\n"
            "https://dvprogram.state.gov/"
        )

    send(
        "ℹ️ DV Lottery site changed.\n\n"
        "🔍 Diff (cleaned text):\n"
        "```\n"
        f"{diff_text}\n"
        "```"
    )

    with open("page_old.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(new_lines))
