import requests
import allure

class PageApi:

    def __init__(self):
        self.base_url = "https://altaivita.ru/engine"

    # Отправить товар в корзину
    @allure.title("API: Отправление товара в корзину")
    def  add_product_to_cart(self, new_headers: dict, new_body: dict):
        """
        Функция выполняет запрос к API для отправки товара в корзину.
        Возвращаемое значение:
        - Функция возвращает status_code запроса
        """
        with allure.step("Запрос на отправку товара в корзину"):
            path = ("{base_url}/cart/add_products_to_cart_from_preview.php".format(base_url=self.base_url))
            resp = requests.post(path, headers=new_headers, data=new_body)
        with allure.step("Возврат инфо о товаре, добавленного в корзину"):
            return  resp.status_code

    # Добавить количествотовара в корзине
    @allure.title("API: Добавление количества товара в корзине")
    def add_product_quantity(self, new_headers: dict, new_body: dict):
        """
        Функция выполняет запрос к API для добаления количества товара в корзине.
        Возвращаемое значение
        - Функция возвращает status_code запроса
        """
        with allure.step("Запрос на добаление количества товара в корзине"):
            path = ("{base_url}/cart/add_products_to_cart_from_preview.php".format(base_url=self.base_url))
            resp = requests.post(path, headers=new_headers, data=new_body)
        with allure.step("Возврат количества добавленного товара"):
            return  resp.status_code
    
    # Получить список жанров
    @allure.title("API: Удаление товара из корзины")
    def remove_product_from_cart(self, new_headers: dict, new_body: dict):
        """
        Функция выполняет запрос к API для удаления товара из корзины.
        Возвращаемое значение
        - Функция возвращает status_code запроса
        """
        with allure.step("Запрос на Удаление товара из корзины"):
            path = ("{base_url}/cart/delete_products_from_cart_preview.php".format(base_url=self.base_url))
            resp = requests.post(path, headers=new_headers, data=new_body)
        with allure.step("Возврат инфо об удаленном товаре"):    
            return  resp.status_code
