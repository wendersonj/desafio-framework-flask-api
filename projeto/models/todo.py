from typing import List

from pydantic import root_validator

from projeto.utils.camel_model import CamelModel

class ToDo(CamelModel):
    id: int
    user_id: str
    title: str
    completed: bool

    @root_validator()
    def test(cls, values):
        # print(values)
        return values


class ToDoList(CamelModel):
    todo_list: List[ToDo]
