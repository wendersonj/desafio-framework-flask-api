from typing import List

import logging
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
    logging.info(f"/get_first_five_todo was requested")
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    # verificar se recebeu uma resposta 200. senão, levanta exceção de servidor do request está com problemas e tente novamente.

    if response.status_code in (200, 201):
        list_of_items = ToDoList(todo_list=parse_obj_as(List[ToDo], response.json()[:5]))
        to_be_return = list_of_items.json(exclude={'todo_list': {'__all__': {'completed': True, 'user_id': True}}})
        logging.info(f"/get_first_five_todo : response content from API: {to_be_return}. status code {response.status_code}")

        return to_be_return

    # tratar os dados em um modelo antes de enviá-los na resposta

    else:
        logging.info(f"/get_first_five_todo : invalid response . status code {response.status_code}")
        return (f'Não foi possível completar sua requisição.'
                f'Tente novamente.')


if __name__ == "__main__":
    logging.basicConfig(filename='api.log', level=logging.DEBUG, format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    app.run()
