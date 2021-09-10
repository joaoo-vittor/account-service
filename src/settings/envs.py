import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_URI = "sqlite:///storage.db"
HASH = os.environ.get("HASH")
