from app import app
from base64 import b64encode


def test_unauthorized_access_response():
    response = app.test_client().get('/get_first_five_todo')

    assert response.status_code == 401




def test_success_response():
    headers = {
        'Authorization': 'Basic ' + b64encode(b"framework:desafio").decode('utf-8')
    }
    response = app.test_client().get('/get_first_five_todo', headers=headers)

    assert response.status_code == 200
    assert response.json.get('todo_list', None) is not None
    assert len(response.json['todo_list']) == 5


def test_invalid_service_response():
    headers = {
        'Authorization': 'Basic ' + b64encode(b"framework:desafio").decode('utf-8')
    }
    response = app.test_client().get('/invalid_service', headers=headers)

    assert response.status_code == 503
    assert response.json.get('error', None) is not None
    assert response.json.get('error')['reason'] is not None
