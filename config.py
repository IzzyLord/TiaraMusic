import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "🎵 𝐓𝐢𝐚𝐫𝐚 𝐌𝐮𝐬𝐢𝐜 🎵")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/d2ed6d40c527aa9fed38b.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/52fc690e945ebb281856d.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/bb3be3074b5c22686c2d2.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/96c8c0b8fe35fc54d4ed6.png")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "TiaraMusic_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "AssistanceMutiara")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "jawravirtul")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "mutiaraindh")
OWNER_NAME = getenv("OWNER_NAME", "Oyhaok") # isi dengan username kamu tanpa simbol @
PMPERMIT = getenv("PMPERMIT", None)
OWNER_ID = int(os.environ.get("OWNER_ID")) # fill with your id as the owner of the bot
DATABASE_URL = os.environ.get("DATABASE_URL") # fill with your mongodb url
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL")) # make a private channel and get the channel id
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False)) # just fill with True or False (optional)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
LANG = getenv("LANG", "id")
