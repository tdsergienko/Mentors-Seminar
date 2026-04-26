from fastapi import FastAPI, HTTPException
from typing import List

from app.database import db
from app.repository import todo_repository, TodoItem
from app.models import TodoCreate, TodoUpdate, TodoResponse

app = FastAPI(title="Todo Service")


@app.on_event("startup")
def startup() -> None:
    db.init()


def to_response(item: TodoItem) -> TodoResponse:
    return TodoResponse(
        id=item.id,
        title=item.title,
        description=item.description,
        completed=item.completed,
    )


@app.post("/items", response_model=TodoResponse)
def create_item(item: TodoCreate):
    created = todo_repository.create(
        title=item.title,
        description=item.description,
        completed=item.completed,
    )
    return to_response(created)


@app.get("/items", response_model=List[TodoResponse])
def get_items():
    items = todo_repository.get_all()
    return [to_response(item) for item in items]


@app.get("/items/{item_id}", response_model=TodoResponse)
def get_item(item_id: int):
    item = todo_repository.get_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return to_response(item)


@app.put("/items/{item_id}", response_model=TodoResponse)
def update_item(item_id: int, item: TodoUpdate):
    updated = todo_repository.update(
        item_id=item_id,
        title=item.title,
        description=item.description,
        completed=item.completed,
    )
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return to_response(updated)


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    deleted = todo_repository.delete(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"status": "deleted"}
