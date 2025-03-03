import sender_stand_request
import data

# Тестовый сценарий для создания и получения заказа
def test_create_and_fetch_order():
    # Создание заказа
    create_response = sender_stand_request.post_new_order(data.order_body)
    assert create_response.status_code == 201, "Не удалось создать заказ."
    
    # Сохранение трек-номера заказа
    track_number = create_response.json().get("track")
    assert track_number, "Неверный ответ сервера. Трек-номер не получен."
    
    # Получение заказа по трек-номеру
    get_response = sender_stand_request.get_order_track(track_number)
    assert get_response.status_code == 200, "Не удалось получить заказ."
    
    # Вывод успешного результата
    print("Тест пройден. Заказ успешно создан и получен.")