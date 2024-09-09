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
        dict: Словарь, содержащий данные о товаре отправленном в корзину.
        """
        with allure.step("Запрос на отправку товара в корзину"):
            path = ("{base_url}/ajax/ajax_ecommerce/ajax_ecommerce".format(base_url=self.base_url))
            resp = requests.post(path, headers=new_headers, payload=new_body)
        with allure.step("Возврат инфо о товаре, добавленного в корзину"):
            return  resp.json()

    # Получить список стран
    @allure.title("API: Добаление количества товара в корзине")
    def add_product_quantity(self, field_name):
        """
        Функция выполняет запрос к API для добаления количества товара в корзине.
        Возвращаемое значение
        - Функция возвращает ответ API в формате JSON, который содержит количество добавленного товара
        """
        with allure.step("Запрос на добаление количества товара в корзине"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.post(path, headers=self.headers)
        with allure.step("Возврат количества добавленного товара"):
            return  resp.json()
    
    # Получить список жанров
    @allure.title("API: Удаление товара из корзины")
    def remove_product_from_cart(self, field_name):
        """
        Функция выполняет запрос к API для удаления товара из корзины.
        Возвращаемое значение
        - `dict`: Функция возвращает ответ API в формате JSON, который содержит информацию об удаленном товре.
        """
        with allure.step("Запрос на Удаление товара из корзины"):
            path = ("{base_url}/movie/possible-values-by-field?field={f_name}".format(base_url=self.base_url, f_name=field_name))
            resp = requests.post(path, headers=self.headers)
        with allure.step("Возврат инфо об удаленном товаре"):    
            return  resp.json()
