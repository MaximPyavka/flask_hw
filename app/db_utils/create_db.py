# chinook.db


import sqlite3
from app.config import dev_config

DB_NAME = 'chinook.db'
DB_DIR = dev_config["BASE_DIR"]+"/db_utils/"+DB_NAME

def connect_db():
    conn = sqlite3.connect(DB_DIR)
    return conn