import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import allure
from pages.PageApi import PageApi

api = PageApi()

@allure.suite("API: Тестирование отправки товара в корзину")
@allure.title("API: Отправить товар в корзину")
def test_add_product_to_cart():
    """
    Функция предназначена для тестирования API, который отправляет товар в корзину.
    - Функция возвращает status_code запроса
    """
    with allure.step("Отправляем товар в корзину"):
        myheaders = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'content-length': '160',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'CID=2039c84b964e51cb378657bd6f5d5cda; site_countryID=247'
        }

        payload = {
            'product_id': 1781,
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': '2039c84b964e51cb378657bd6f5d5cda',
            'S_cur_code': 'rub',
            'S_koef': 1,
            'quantity': 1
        }

        status_code = api.add_product_to_cart(myheaders, payload)
    with allure.step("Проверить, что список не пустой"):
        assert status_code == 200

@allure.suite("API: Тестирование добавления количества товара в корзине")
@allure.title("API: Добавить количество товара в корзине")
def test_add_product_quantity():
    """
    Функция предназначена для тестирования API, добавляет уоличество товара в корзине.
    - Функция возвращает status_code запроса
    """
    with allure.step("Добавляем количество товара в корзине"):
        myheaders = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'CID=2039c84b964e51cb378657bd6f5d5cda; site_countryID=247'
        }

        payload = {
            'product_id': 1781,
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': '2039c84b964e51cb378657bd6f5d5cda',
            'S_cur_code': 'rub',
            'S_koef': 1,
            'quantity': 1,
            'S_hint_code': '',
            'S_customerID': ''
        }

        status_code = api.add_product_quantity(myheaders, payload)
    with allure.step("Проверить, что список не пустой"):
        assert status_code == 200

@allure.suite("API: Тестирование удаления товара из корзины")
@allure.title("API: Удаление товара из корзины")
def test_remove_product_from_cart():
    """
    Функция предназначена для тестирования API, удаляет ьовар из корзины.
    - Функция возвращает status_code запроса
    """
    with allure.step("Удаляем товар из корзине"):
        myheaders = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'CID=2039c84b964e51cb378657bd6f5d5cda; site_countryID=247'
        }

        payload = {
            'product_id': 1781,
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': '2039c84b964e51cb378657bd6f5d5cda',
            'S_cur_code': 'rub',
            'S_koef': 1,
            'S_hint_code': '',
            'S_customerID': ''
        }

        status_code = api.remove_product_from_cart(myheaders, payload)
    with allure.step("Проверить, что список не пустой"):
        assert status_code == 200