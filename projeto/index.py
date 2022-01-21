from typing import List

import requests
from flask import Flask
from pydantic import parse_obj_as, root_validator

from projeto.utils.camel_model import CamelModel

app = Flask("Desafio Python - Framework")


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


@app.route('/get_first_five_todo')
def get_first_five_todo():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    # verificar se recebeu uma resposta 200. senão, levanta exceção de servidor do request está com problemas e tente novamente.

    if response.status_code in (200, 201):
        list_of_items = ToDoList(todo_list=parse_obj_as(List[ToDo], response.json()[:5]))
        return list_of_items.json(exclude={'todo_list': {'__all__': {'completed': True, 'user_id': True}}})

    # tratar os dados em um modelo antes de enviá-los na resposta

    else:
        return (f'Não foi possível completar sua requisição.'
                f'Tente novamente.')


app.run()
