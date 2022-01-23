from typing import List

import logging
import requests
from flask import Flask, Response, make_response
from pydantic import parse_obj_as

from projeto.models.todo import ToDoList, ToDo
from projeto.utils.camel_model import CamelModel

app = Flask("Desafio Python - Framework")
app.debug = True


class ErrorMessage(CamelModel):
    error: str
    reason: str


@app.route('/get_first_five_todo')
def get_first_five_todo():
    logging.info(f"/get_first_five_todo was requested")
    response_placeholder = requests.get('https://jsonplaceholder.typicode.com/todos')
    # verificar se recebeu uma resposta 200. senão, levanta exceção de servidor do request está com problemas e tente novamente.

    if response_placeholder.status_code in (5, 6):
        list_of_items = ToDoList(todo_list=parse_obj_as(List[ToDo], response_placeholder.json()[:5]))
        todo_list = list_of_items.json(exclude={'todo_list': {'__all__': {'completed': True, 'user_id': True}}})

        response = Response(todo_list, content_type="application/json; charset=utf-8", status=200)
        log_response_content('/get_first_five_todo', response, logging.info)

        return response

    # tratar os dados em um modelo antes de enviá-los na resposta

    else:
        logging.info(
            f"/get_first_five_todo : invalid response from placeholder.typicode with "
            f"status code {response_placeholder.status_code}")

        error = ErrorMessage(error="Serviço indisponível",
                             reason="Não foi possível completar sua requisição. Tente novamente.")

        response = Response(error.json(), content_type="application/json; charset=utf-8", status=503)

        log_response_content('/get_first_five_todo', response, logging.info)

        return response


def log_response_content(route, response, logger_with_level):
    logger_with_level(f'{route}: raw response content from API: {response}. status code {response.status_code}')


if __name__ == "__main__":
    logging.basicConfig(filename='api.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - [%(levelname)s] -  %(message)s')
    logging.getLogger('werkzeug').setLevel(logging.CRITICAL)
    app.run()
