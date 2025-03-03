import configuration
import requests
from data import order_body

# Запрос на создание заказа.
def post_new_order(order_body):
    url = configuration.URL_SERVICE + configuration.CREATE_ORDERS
    response = requests.post(url, json=order_body)
    return response

# Запрос на получение заказа по его трек-номеру.
def get_order_track(track_number):
    url = f"{configuration.URL_SERVICE}{configuration.ORDER_TRACK}?t={track_number}"
    response = requests.get(url)
    return response