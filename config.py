import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6907928203:AAEZSDjgfwyVFqFmxBaXAItfIA-XKHAQw58")

    APP_ID = int(os.environ.get("APP_ID", 26384753))

    API_HASH = os.environ.get("API_HASH", "d0df15edaf47d46b36747f8af2e11b6f")
