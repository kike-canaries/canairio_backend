import pyrebase

from django.conf import settings


def noquote(s):
    return s


pyrebase.pyrebase.quote = noquote

config = {
    "apiKey": settings.FB_API_KEY,
    "authDomain": settings.FB_AUTH_DOMAIN,
    "databaseURL": settings.FB_DATABASE_URL,
    "storageBucket": settings.FB_STORAGE_BUCKET
}

firebase = pyrebase.initialize_app(config)

firebase_db = firebase.database()
