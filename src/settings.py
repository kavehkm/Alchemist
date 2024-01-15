# standard
import json
from pathlib import Path


# settings.json file path
settings_path = Path(__file__).resolve().parent.parent / "settings.json"


# load settings from settings.json
try:
    with open(settings_path, "rt") as f:
        settings = json.loads(f.read())
except Exception:
    settings = {}


IP = settings.get("ip")
PORT = settings.get("port")
DATABASE = settings.get("database")
USER = settings.get("user")
PASSWORD = settings.get("password")
CHARSET = settings.get("charset")
ECHO = settings.get("echo")
