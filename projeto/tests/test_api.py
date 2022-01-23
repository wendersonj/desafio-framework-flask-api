from projeto.app import app


def test_success_response():
    response = app.test_client().get('/get_first_five_todo')

    assert response.status_code == 200
    assert 'todo_list' in response.json.keys()
    assert len(response.json['todo_list']) == 5
