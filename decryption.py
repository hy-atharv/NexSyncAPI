import os
import dotenv
from dotenv import load_dotenv
from cryptography.fernet import Fernet

load_dotenv()

key = os.getenv('FERNET_KEY')

f = Fernet(key)
token = 'gAAAAABlupZpVNd5UacDZuo4c_PH2T-Z79BuX43b_zPQu9g9_FiMtXV5tHKo0ws8pwAmWHlMnQGVnxR76XBXkQNfcCn6t45AnGB_elFAziVgKipJ4nNWLMs='


def Decrypt(token):
    d = f.decrypt(token)
    return d.decode()
