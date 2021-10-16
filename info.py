import os
from os import environ

API_ID = int(os.environ.get("API_ID", 12345))
API_HASH = os.environ.get("API_HASH", None)
SESSION = os.environ.get("SESSION")
ADMINS = set(int(x) for x in os.environ.get("ADMINS", "1914275867").split())
TIME = os.environ.get("TIME", None)
GROUPS = [int(admin) for admin in environ.get("GROUPS", "").split()]
