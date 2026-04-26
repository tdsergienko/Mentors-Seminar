import requests

BASE_URL = "http://localhost:8000"


def test_create_item():
    r = requests.post(
        f"{BASE_URL}/items",
        json={"title": "Docker todo"},
    )
    assert r.status_code == 200

    data = r.json()
    assert "id" in data
    assert data["title"] == "Docker todo"


def test_get_items():
    r = requests.get(f"{BASE_URL}/items")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_update_item():
    create = requests.post(
        f"{BASE_URL}/items",
        json={"title": "Old title"},
    )
    item_id = create.json()["id"]

    update = requests.put(
        f"{BASE_URL}/items/{item_id}",
        json={"title": "New title", "completed": True},
    )
    assert update.status_code == 200
    assert update.json()["completed"] is True


def test_delete_item():
    create = requests.post(
        f"{BASE_URL}/items",
        json={"title": "To delete"},
    )
    item_id = create.json()["id"]

    delete = requests.delete(f"{BASE_URL}/items/{item_id}")
    assert delete.status_code == 200

    get_after = requests.get(f"{BASE_URL}/items/{item_id}")
    assert get_after.status_code == 404
