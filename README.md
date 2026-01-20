# DV Lottery Monitor (Telegram Alerts)

This project monitors the official U.S. Diversity Visa (Green Card Lottery) website and sends **Telegram notifications** when meaningful changes occur.

It is designed to avoid noise and only alert when **important updates** (such as the opening of the entry period) appear.

---

## Features

- Daily automatic checks via GitHub Actions
- Telegram notifications
- Smart HTML cleanup (ignores scripts, styles, metadata)
- Text-based diff of real content changes
- High-priority alerts for important keywords
- No servers required (runs 100% on GitHub)

---

## What is monitored

Official website: https://dvprogram.state.gov/

---

## Important keyword detection

The bot looks for keywords such as:

- `entry period`
- `is now open`
- `dv-202*`
- `check status`
- `submit`

If any of these appear in new changes, a **high-priority alert** is sent.

---

## How it works (high level)

1. GitHub Actions runs once per day
2. Downloads the DV Lottery page
3. Cleans HTML (removes scripts, styles, tags)
4. Compares visible text with the previous version
5. Generates a diff
6. Sends Telegram alerts if changes are detected
7. Saves the new version for future comparisons

---

## Schedule

The workflow runs **once per day at 08:00 UTC**  
(Manual execution is also available via GitHub Actions UI)

---

## Setup instructions

### 1. Create a Telegram bot
- Open Telegram
- Talk to **@BotFather**
- Create a bot and copy the **BOT_TOKEN**

### 2. Get your chat ID
Send a message to your bot, then open: https://api.telegram.org/bot<BOT_TOKEN>/getUpdates

### 3. Add GitHub Secrets=
In your repository: Settings → Secrets and variables → Actions
Add:
| Name | Value |
|----|------|
| BOT_TOKEN | Telegram bot token |
| CHAT_ID | Your chat ID |
