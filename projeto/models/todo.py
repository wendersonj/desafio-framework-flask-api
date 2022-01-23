from typing import List
from projeto.utils.camel_model import CamelModel


class ToDo(CamelModel):
    id: int
    user_id: str
    title: str
    completed: bool


class ToDoList(CamelModel):
    todo_list: List[ToDo]
