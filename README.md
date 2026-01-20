# DV Lottery Monitor (Telegram Alerts)

This project monitors **official U.S. visa news** and sends a **Telegram notification** when a **new announcement appears** that may affect the Diversity Visa (Green Card Lottery).

The goal is simple and reliable:
**detect a new official announcement → notify → manually check the DV Lottery site**.

No noise. No diffs. No false alerts.

---

## 🎯 What this project does

- Checks the official **U.S. Visas News** page
- Extracts **only the latest news item**
- Compares it with the previously stored one
- If the news has changed:
  - Sends the **news title** to Telegram
  - Sends a link to the **DV Lottery main page** for manual verification

---

## 🚀 Features

- ✅ Daily automatic checks via GitHub Actions
- ✅ Telegram notifications
- ✅ Monitors only **official announcements**
- ✅ Stores only **one value** (latest news)
- ✅ No HTML diff, no keyword noise
- ✅ No servers required (100% GitHub-hosted)

---

## 🔍 What is monitored

**Primary source (official):**  
https://travel.state.gov/content/travel/en/News/visas-news.html

**Manual verification link (sent on alert):**  
https://dvprogram.state.gov/

---

## 🧠 Why this approach

- Important DV updates are **always published as new announcements**
- Old news is not edited — new events create new entries
- Monitoring only the latest item is:
  - more reliable
  - easier to maintain
  - immune to Cloudflare blocks
- The DV Lottery site itself is best checked **manually** once an alert appears

---

## ⚙️ How it works (high level)

1. GitHub Actions runs once per day
2. Downloads the *U.S. Visas News* page
3. Extracts the **most recent news item**
4. Compares it with the previously saved one
5. If it changed:
   - Sends the news title to Telegram
   - Sends a link to the DV Lottery website
6. Saves the new item for the next run

---

## 🕗 Schedule

The workflow runs **once per day at 08:00 UTC**  
Manual execution is also available via the GitHub Actions UI.

---

## 🛠️ Setup instructions

### 1. Create a Telegram bot
- Open Telegram
- Talk to **@BotFather**
- Create a bot
- Copy the **BOT_TOKEN**

### 2. Get your chat ID
- Send any message to your bot
- Open: https://api.telegram.org/bot<BOT_TOKEN>/getUpdates
- Find your `chat.id`.

### 3. Add GitHub Secrets

In your repository: Settings → Secrets and variables → Actions

Add the following secrets:

| Name       | Value                  |
|------------|------------------------|
| BOT_TOKEN  | Telegram bot token     |
| CHAT_ID    | Your Telegram chat ID  |
