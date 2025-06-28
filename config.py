import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
CHANNEL_LINK = os.getenv("CHANNEL_LINK")
PAYMENT_LINK = os.getenv("PAYMENT_LINK")
SUBSCRIPTION_DAYS = int(os.getenv("SUBSCRIPTION_DAYS"))
GRACE_PERIOD_DAYS = int(os.getenv("GRACE_PERIOD_DAYS"))
ADMIN_ID = int(os.getenv("ADMIN_ID"))
