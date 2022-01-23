from projeto.index import app


def test_success_response():
    response = app.test_client().get('/get_first_five_todo')

    assert response.status_code == 200
    assert response.json.get('todo_list', None) is not None
    assert len(response.json['todo_list']) == 5
