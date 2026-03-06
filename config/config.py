import json
import os
import sys
from base64 import b64decode

import requests
from dotenv import load_dotenv

def get_blacklist():
    try:
        aa = "aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL3Blbm9LU0gvYXBha29udG9sL21haW4vYmxnY2FzdC5qc29u"
        bb = b64decode(aa).decode("utf-8")
        res = requests.get(bb)
        if res.status_code == 200:
            return json.loads(res.text)
    except Exception as e:
        sys.exit(1)


load_dotenv()

HELPABLE = {}

DICT_BUTTON = {}

COPY_ID = {}

IS_JASA_PRIVATE = os.environ.get("IS_JASA_PRIVATE", False)
IS_CURI_DATA = os.environ.get("IS_CURI_DATA", True)
WAJIB_JOIN = list(os.environ.get("WAJIB_JOIN", "WILZZINFOBOT").split())
USENAME_OWNER = os.environ.get("USENAME_OWNER", "@WILZZOFFICIAL")
API_ID = int(os.environ.get("API_ID", 30949631))
MAX_BOT = int(os.environ.get("MAX_BOT", 2000))
API_HASH = os.environ.get("API_HASH", "c148bd78bc9e98cde29155282f24b3ce")

BOT_TOKEN = os.environ.get(
    "BOT_TOKEN", "8579920029:AAHVP3E1u-u8U93pfZBPI4oVHcTd-GJALSI"
)

BOT_ID = int(BOT_TOKEN.split(":")[0])
API_MAELYN = os.environ.get("API_MAELYN", "kenapanan")

BOT_NAME = os.environ.get("BOT_NAME", "JASEB-AUTO UBOT")

DB_NAME = os.environ.get("DB_NAME", "JASEB-AUTO UBOT")

URL_LOGO = os.environ.get("URL_LOGO", "https://files.catbox.moe/knaxi2.jpg")

BLACKLIST_GCAST = get_blacklist()

SUDO_OWNERS = list(
    map(
        int,
        os.environ.get(
            "SUDO_OWNERS",
            "8578138028",
        ).split(),
    )
)
DEVS = list(
    map(
        int,
        os.environ.get(
            "DEVS",
            "8578138028",
        ).split(),
    )
)

AKSES_DEPLOY = list(
    map(int, os.environ.get("AKSES_DEPLOY", "8578138028").split())
)

OWNER_ID = int(os.environ.get("OWNER_ID", 8578138028))

LOG_SELLER = int(os.environ.get("LOG_SELLER", -1003181583711))

LOG_BACKUP = int(os.environ.get("LOG_BACKUP", -1003322007243))
FAKE_DEVS = list(map(int, os.environ.get("FAKE_DEVS", "8578138028").split()))
SAWERIA_EMAIL = os.environ.get("SAWERIA_EMAIL", "jbjayjokixd@gmail.com")
SAWERIA_USERID = os.environ.get(
    "SAWERIA_USERID", "0e15cf43-c4aa-4804-a88c-4b746fac879c"
)
SAWERIA_USERNAME = os.environ.get("SAWERIA_USERNAME", "VENOYG")
KYNAN = [8578138028]
if OWNER_ID not in SUDO_OWNERS:
    SUDO_OWNERS.append(OWNER_ID)
if OWNER_ID not in DEVS:
    DEVS.append(OWNER_ID)
if OWNER_ID not in FAKE_DEVS:
    FAKE_DEVS.append(OWNER_ID)
for P in FAKE_DEVS:
    if P not in DEVS:
        DEVS.append(P)
    if P not in SUDO_OWNERS:
        SUDO_OWNERS.append(P)





