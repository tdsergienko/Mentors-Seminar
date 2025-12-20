import sqlite3
import os

DATABASE_PATH = "/app/data/todo.db"
TODO_DB_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    completed INTEGER NOT NULL DEFAULT 0
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
            cursor.execute(TODO_DB_CREATE_TABLE)
            conn.commit()


db = Database(DATABASE_PATH)
