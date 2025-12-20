import requests

BASE_URL = "http://localhost:8001"


def test_shorten_url():
    response = requests.post(
        f"{BASE_URL}/shorten",
        json={"url": "https://example.com"},
    )

    assert response.status_code == 200

    data = response.json()
    assert "short_url" in data
    assert data["short_url"].startswith("/")


def test_redirect():
    create = requests.post(
        f"{BASE_URL}/shorten",
        json={"url": "https://example.com"},
    )
    short_path = create.json()["short_url"]

    response = requests.get(
        f"{BASE_URL}{short_path}",
        allow_redirects=False,
    )

    assert response.status_code in (301, 302, 307)
    assert response.headers["location"] == "https://example.com/"


def test_stats():
    create = requests.post(
        f"{BASE_URL}/shorten",
        json={"url": "https://example.org"},
    )
    short_id = create.json()["short_url"].lstrip("/")

    stats = requests.get(f"{BASE_URL}/stats/{short_id}")
    assert stats.status_code == 200

    data = stats.json()
    assert data["short_id"] == short_id
    assert data["full_url"] == "https://example.org/"


def test_not_found_redirect():
    response = requests.get(
        f"{BASE_URL}/nonexistent",
        allow_redirects=False,
    )

    assert response.status_code == 404


def test_not_found_stats():
    response = requests.get(f"{BASE_URL}/stats/nonexistent")
    assert response.status_code == 404
