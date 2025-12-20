import sqlite3
import os

DATABASE_PATH = "/app/data/shorturl.db"

SHORTURL_DB_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    short_id TEXT NOT NULL UNIQUE,
    full_url TEXT NOT NULL
)
"""


class Database:
    def __init__(self, database_path: str):
        self.path = database_path
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.path, check_same_thread=False)

    def init(self) -> None:
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SHORTURL_DB_CREATE_TABLE)
            conn.commit()


db = Database(DATABASE_PATH)
