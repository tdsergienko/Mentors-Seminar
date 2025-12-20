import string
import random
from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from app.database import db
from app.repository import shorturl_repository
from app.models import ShortenRequest, ShortenResponse, ShortUrlStats

app = FastAPI(title="Short URL Service")


@app.on_event("startup")
def startup() -> None:
    db.init()


def generate_short_id(length: int = 6) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(random.choices(alphabet, k=length))


@app.post("/shorten", response_model=ShortenResponse)
def shorten_url(request: ShortenRequest):
    short_id = generate_short_id()

    shorturl_repository.create(
        short_id=short_id,
        full_url=str(request.url),
    )

    return ShortenResponse(short_url=f"/{short_id}")


@app.get("/{short_id}")
def redirect(short_id: str):
    item = shorturl_repository.get_by_short_id(short_id)
    if not item:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url=item.full_url)


@app.get("/stats/{short_id}", response_model=ShortUrlStats)
def stats(short_id: str):
    item = shorturl_repository.get_by_short_id(short_id)
    if not item:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return ShortUrlStats(
        short_id=item.short_id,
        full_url=item.full_url,
    )
