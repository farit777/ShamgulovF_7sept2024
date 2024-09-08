import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
import allure
from pages.PageUi import PageUi

@allure.suite("UI: Тестирование кнопки 'В корзину'")
@allure.title("UI: Проверка клика по кнопке 'В корзину'")
def test_click_to_cart(prod_page: PageUi):
    """
    Функция предназначена для проверки нажатия кнопки "В корзину" у товара "Огневка Люкс".
    Она отправляет товр в корзину.
    """
    with allure.step("Кликнуть по кнопке 'В корзину'"):
        prod_page.click_to_cart()
    with allure.step("Проверить что в корзине появился товар"):
        assert prod_page.count_prods > 0

@allure.suite("UI: тестирование добавления количества в корзине")
@allure.title("UI: Проверка добавления количества в корзине")
def test_increase_quantity(prod_page: PageUi):
    """
    Функция предназначена для проверки нажатия кнопки '+' у товара "Огневка Люкс".
    Она увеличивает количество товара в корзине.
    """
    with allure.step("Кликнуть по кнопке '+'"):
        prod_page.increase_quantity()
    with allure.step("Проверить что в корзине товаров > 1"):
        assert prod_page.count_prods > 0

@allure.suite("UI: тестирование удаления товра из корзиные")
@allure.title("UI: Проверка добавления количества в корзине")
def test_remove_item_from_cart(prod_page: PageUi):
    """
    Функция предназначена для проверки удаления товара из корзины".
    Она удаляет товар из корзины.
    """
    with allure.step("Кликнуть по кнопке 'Х'"):
        prod_page.remove_item_from_cart()
    with allure.step("Проверить что в корзине товаров = 0"):
        assert prod_page.count_prods == 0