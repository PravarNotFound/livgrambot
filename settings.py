import os
from dotenv import load_dotenv, find_dotenv

# Loading .env variables
load_dotenv(find_dotenv())

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if TELEGRAM_TOKEN is None:
    raise Exception("Please setup the .env variable TELEGRAM_TOKEN.")

PORT = int(os.environ.get('PORT', '8443'))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")

TELEGRAM_SUPPORT_CHAT_ID = os.getenv("TELEGRAM_SUPPORT_CHAT_ID")
if TELEGRAM_SUPPORT_CHAT_ID is None or not str(TELEGRAM_SUPPORT_CHAT_ID).lstrip("-").isdigit():
    raise Exception("You need to specify 'TELEGRAM_SUPPORT_CHAT_ID' env variable: The bot will forward all messages to this chat_id. Add this bot https://t.me/ShowJsonBot to your private chat to find its chat_id.")
TELEGRAM_SUPPORT_CHAT_ID = int(TELEGRAM_SUPPORT_CHAT_ID)


WELCOME_MESSAGE = os.getenv("WELCOME_MESSAGE", "**Hey buddy** [👋](https://te.legra.ph/file/88a636de87d2c2583d469.mp4)

⛔ **You can contact with us using this bot.**

⭕ 𝗥𝗘𝗠𝗘𝗠𝗕𝗘𝗥 
   **• No invite links**
   **• No selling**
   **• No bot refferal links**
   **• No abusing**

**Jᴜꜱᴛ Dʀᴏᴘ Yᴏᴜʀ Mᴇꜱꜱᴀɢᴇ Hᴇʀᴇ** ↙️⤵️

[📛 𝑱𝑶𝑰𝑵 𝑶𝑼𝑹 𝑶𝑭𝑭𝑰𝑪𝑰𝑨𝑳 𝑮𝑹𝑶𝑼𝑷 📛](https://t.me/+gSrp0a_3QAliNzM9)

")
REPLY_TO_THIS_MESSAGE = os.getenv("REPLY_TO_THIS_MESSAGE", "REPLY_TO_THIS")
WRONG_REPLY = os.getenv("WRONG_REPLY", "WRONG_REPLY")
