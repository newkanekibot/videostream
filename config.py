import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Video Stream")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "Cyberhunt27")
ALIVE_NAME = getenv("ALIVE_NAME", "cyberhunt")
BOT_USERNAME = getenv("BOT_USERNAME", "kanekivideobot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kanekiassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TebBotSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TebMusicUpdate")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/77a07f0ea632980299d51.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "240"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/newkanekibot/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/0e333f611af7adcbf3c42.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/49ac0c33e0f9466934427.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/2e4f0f1b8ad1735a0c504.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/9a8ebeebc6951eb8c47d6.png")
