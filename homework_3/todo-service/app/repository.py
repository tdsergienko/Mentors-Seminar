from typing import List, Optional
from app.database import db
from dataclasses import dataclass

TODO_DB_GET_ALL = """
SELECT id, title, description, completed FROM items
"""
TODO_DB_GET_BY_ID = """
SELECT id, title, description, completed FROM items WHERE id = ?
"""
TODO_DB_CREATE = """
INSERT INTO items (title, description, completed) VALUES (?, ?, ?)
"""
TODO_DB_UPDATE = """
UPDATE items 
    SET title = ?, description = ?, completed = ?
    WHERE id = ?
"""
TODO_DB_DELETE_BY_ID = """
DELETE FROM items WHERE id = ?
"""


@dataclass
class TodoItem:
    id: int
    title: str
    description: Optional[str]
    completed: bool


class TodoRepository:
    def get_all(self) -> List[TodoItem]:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(TODO_DB_GET_ALL)
            rows = cursor.fetchall()

        return [
            TodoItem(
                id=row[0],
                title=row[1],
                description=row[2],
                completed=bool(row[3]),
            )
            for row in rows
        ]

    def get_by_id(self, item_id: int) -> Optional[TodoItem]:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(TODO_DB_GET_BY_ID, (item_id,))
            row = cursor.fetchone()

        if not row:
            return None

        return TodoItem(
            id=row[0],
            title=row[1],
            description=row[2],
            completed=bool(row[3]),
        )

    def create(
        self,
        title: str,
        description: Optional[str],
        completed: bool = False,
    ) -> TodoItem:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(TODO_DB_CREATE, (title, description, int(completed)))
            item_id = cursor.lastrowid

        return TodoItem(
            id=item_id,
            title=title,
            description=description,
            completed=completed,
        )

    def update(
        self,
        item_id: int,
        title: Optional[str],
        description: Optional[str],
        completed: Optional[bool],
    ) -> Optional[TodoItem]:
        item = self.get_by_id(item_id)
        if not item:
            return None

        new_title = title if title is not None else item.title
        new_description = description if description is not None else item.description
        new_completed = completed if completed is not None else item.completed

        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                TODO_DB_UPDATE,
                (new_title, new_description, int(new_completed), item_id),
            )

        return TodoItem(
            id=item_id,
            title=new_title,
            description=new_description,
            completed=new_completed,
        )

    def delete(self, item_id: int) -> bool:
        with db.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(TODO_DB_DELETE_BY_ID, (item_id,))
            return cursor.rowcount > 0


todo_repository = TodoRepository()
