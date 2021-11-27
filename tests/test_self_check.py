def test_self_check(client):
    """
    Тест, который проверяет запустился ли FastAPI вообще или нет
    """
    response = client.get('/self_check')

    assert response.status_code == 200
