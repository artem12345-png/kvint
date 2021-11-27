def test_speach(client):
    response = client.get('/send_msg/HI/1')
    assert response.status_code == 200
    assert response.text == 'Какую вы хотите пиццу? Большую или маленькую?'

    response = client.get('/send_msg/большую/1')
    assert response.status_code == 200
    assert response.text == 'Как вы будете оплачивать?'

    response = client.get('/send_msg/наличкой/1')
    assert response.status_code == 200
    assert response.text == 'Вы хотите большую пиццу, оплата - наличкой?'

    response = client.get('/send_msg/да/1')
    assert response.status_code == 200
    assert response.text == 'Спасибо за заказ'
