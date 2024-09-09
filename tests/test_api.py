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
    Тест проверяет, что ...  .
    """
    with allure.step("Получить список список фильмов по названию"):
        myheaders = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br, zstd',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'connection': 'keep-alive',
            'content-length': '160',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'CID=2039c84b964e51cb378657bd6f5d5cda; site_countryID=247'
        }

        payload1 = {
            'product_id': 1781,
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': '2039c84b964e51cb378657bd6f5d5cda',
            'S_cur_code': 'rub',
            'S_koef': 1,
            'quantity': 1
        }

        payload2 = {
            'action': 'ecom_link_products_cart',
            'productID': 1781,
            'LANG_key': 'ru',
            'S_wh': 1,
            'S_CID': '2039c84b964e51cb378657bd6f5d5cda',
            'S_cur_code': 'rub',
            'S_koef': 1
        }
        result = api.add_product_to_cart(myheaders, payload2)
    with allure.step("Проверить, что список не пустой"):
        assert len(result) > 0
