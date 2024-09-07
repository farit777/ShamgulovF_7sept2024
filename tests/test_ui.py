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

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'Годы' на странице фильмов")
def test_check_years(prod_page: PageUi):
    """
    Функция предназначена для проверки корректности работы страницы "Годы" на сайте фильмов.
    Она выполняет переход на страницу годов и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Годы'"):
        prod_page.open_years()
    with allure.step("Проверить загрузку страницы"):
        assert prod_page.browser.current_url == "https://www.kinopoisk.ru/lists/categories/movies/7/"

@allure.suite("UI: тестирование КИНОПОИСК")
@allure.title("UI: Проверка 'критика' на странице фильмов")
def test_check_critics(prod_page: PageUi):
    """
    Функция предназначена для проверки корректности работы страницы "Критика" на сайте фильмов.
    Она выполняет переход на страницу критиков и проверяет, что URL загруженной страницы соответствует ожидаемому значению.
    """
    with allure.step("Перейти на страницу 'Критика'"):
        prod_page.open_critics()
    with allure.step("Проверить загрузку страницы"):
        assert prod_page.browser.current_url == "https://www.kinopoisk.ru/lists/categories/movies/18/"

