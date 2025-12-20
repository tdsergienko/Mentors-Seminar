from typing import Optional
from dataclasses import dataclass
from app.database import db

SHORTURL_DB_GET_BY_SHORT_ID = """
SELECT short_id, full_url FROM urls WHERE short_id = ?
"""

SHORTURL_DB_CREATE = """
INSERT INTO urls (short_id, full_url) VALUES (?, ?)
"""


@dataclass
class ShortUrl:
    short_id: str
    full_url: str


class ShortUrlRepository:
    def get_by_short_id(self, short_id: str) -> Optional[ShortUrl]:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SHORTURL_DB_GET_BY_SHORT_ID, (short_id,))
            row = cursor.fetchone()

        if not row:
            return None

        return ShortUrl(short_id=row[0], full_url=row[1])

    def create(self, short_id: str, full_url: str) -> ShortUrl:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(SHORTURL_DB_CREATE, (short_id, full_url))
            conn.commit()

        return ShortUrl(short_id=short_id, full_url=full_url)


shorturl_repository = ShortUrlRepository()
