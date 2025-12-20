from pydantic import BaseModel, HttpUrl


class ShortenRequest(BaseModel):
    url: HttpUrl


class ShortenResponse(BaseModel):
    short_url: str


class ShortUrlStats(BaseModel):
    short_id: str
    full_url: HttpUrl
