import os

# Stolen from https://github.com/DevsExpo/CrackingToolsBot/blob/main/BotConfig.py :>
# Dont Bulli me.

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    BANNED_ID = os.environ.get("BANNED_ID", None)
    DB_URI = os.environ.get("DATABASE_URL", None)
    API_HASH = os.environ.get("API_HASH", None)
    API_ID = int(os.environ.get("APP_ID", 6))
    LOG_CHAT = int(os.environ.get("LOG_CHAT", -111111))
    OWNER_ID = int(os.environ.get("OWNER_ID", None))
    JTU_ENABLE = os.environ.get("JTU_ENABLE", False)
    JTU_ID = int(os.environ.get("JTU_ID", False))
    JTU_LINK = os.environ.get("JTU_LINK", "t.me/PutLinkHereNIbbaElseHowPeopleWillKnow")
