# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("APP_ID","28985353"))
    API_HASH = os.environ.get("API_HASH","4e42d7f5a246adc4af1d2b1ee4165901")
    BOT_TOKEN = os.environ.get("BOT_TOKEN","7455721193:AAGbss3pPWYyJHAmD0T8zd-fpY0uMRIvBCc")
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", "-1002172724499"))
    BOT_OWNER = int(os.environ.get("BOT_OWNER","7355202955"))
    MONGODB_URL = os.environ.get("MONGODB_URL","mongodb+srv://drglitchoff:qfOE5ZPeLEUIT3M6@cluster0.5hfvlce.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN","cdtKHJVJ05TknMEQRKvZ32pMFHViVpmM")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6
