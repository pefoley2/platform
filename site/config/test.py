import os

SEND_EMAIL = True
EMAIL_FROM = "test@teensforteens.info"
APP_NAME = "Teens for Teens"
SECRET_KEY = "key"

SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(32))
STRIPE_KEY_SECRET = os.getenv("STRIPE_KEY_SECRET", "")
STRIPE_KEY_PUBLIC = os.getenv("STRIPE_KEY_PUBLIC", "")

DB_PATH = "/home/protected/tft.db"

EMAIL_ERRORS = False
SITE_ADMIN = ['foxwilson123@gmail.com']

SERVER_NAME = "test.teensforteens.info"
