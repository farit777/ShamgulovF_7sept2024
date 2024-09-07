import pytest
from selenium import webdriver
from pages.PageUi import PageUi

@pytest.fixture(scope='module')
def browser():
    """
    Функция `browser` - это фикстура для тестирования с использованием Selenium WebDriver.
    Фикстура создаёт экземпляр браузера Chrome с заданными параметрами и обеспечивает его корректное завершение после выполнения тестов.
    Возвращаемое значение:
    WebDriver: Возвращает объект WebDriver для браузера Chrome, который можно использовать в тестах.
    """
    options = webdriver.ChromeOptions()
    options.browser_version = 'stable'
    options.platform_name = 'any'
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(4)
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture(scope='module')
def prod_page(browser):
    """
    Функция `prod_page` - это фикстура для тестирования страницы товаров, используется вместе с Selenium WebDriver.
    Фикстура создаёт экземпляр страницы товаров.
    Возвращаемое значение:
    prod_page: Возвращает объект страницы 'Щитовидная железа'.
    """
    prod_page = PageUi(browser)
    prod_page.open()
    yield prod_page





