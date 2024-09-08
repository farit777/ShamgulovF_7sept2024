from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from time import sleep

class PageUi:
    def __init__(self, browser: WebDriver):
        self.browser = browser
        self.url = "https://altaivita.ru/tag/thyroid/"
        self.count_prods = 0

    @allure.step("Открываем страницу 'Щитовидная железа'")
    def open(self):
        """Открывает страницу 'Щитовидная железа'"""
        self.browser.get(self.url)

    @allure.step("Получим количество товаров в корзине")
    def get_item_count(self):
        self.browser.get("https://altaivita.ru/cart/")
        try:
            # Ожидание, пока кнопка "В корзину" станет кликабельной
            wait = WebDriverWait(self.browser, 5)  # Таймаут в 10 секунд
            # Ждем когда список станет видимым и находим элемент списка товаров в корзине
            basket_list  = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[1]/div[1]/div[2]/div[1]")))
            # Находим все дочерние элементы (товары) в корзине
            basket_items = basket_list.find_elements(By.XPATH, "./div[@class='basket__item js-cart-item']")
            # Получаем и возвращаем количество товаров в корзине
            return len(basket_items)
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            return 0

    @allure.step("Клик по кнопке 'В корзину' товар 'Огневка Люкс'")
    def click_to_cart(self):
        """Отправляет товар в корзину"""
        try:
            # Ожидание, пока кнопка "В корзину" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[5]/div[1]/div[4]/div/div[4]/div/div[2]/div[1]/button')))  # Замените на ваш XPath
            # Клик по кнопке
            button.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        count_prods = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.count.js-count-number.active')))
        self.count_prods = int(count_prods.text)


    @allure.step("Проверка увеличения количества товара")
    def increase_quantity(self):
        "Отправляем товар в корзину"
        try:
            # Ожидание, пока кнопка "В корзину" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            btn_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[5]/div[1]/div[4]/div/div[4]/div/div[2]/div[1]/button')))
            # Клик по кнопке
            btn_to_cart.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        "Увеличиваем количество на 1"
        try:
            # Ожидание, пока кнопка "+" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            btn_plus = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[5]/div[1]/div[4]/div/div[4]/div/div[2]/div[2]/button[2]')))
            # Клик по кнопке
            btn_plus.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        count_prods = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.count.js-count-number.active')))
        self.count_prods = int(count_prods.text)

    @allure.step("Проверка удаления товара из корзины")
    def remove_item_from_cart(self):
        "Отправляем товар в корзину"
        try:
            # Ожидание, пока кнопка "В корзину" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            btn_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[5]/div[1]/div[4]/div/div[4]/div/div[2]/div[1]/button')))
            # Клик по кнопке
            btn_to_cart.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        "Кликаем по кнопке 'Корзина'"
        try:
            # Ожидание, пока кнопка "Корзина" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            btn_plus = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div[1]/div[1]/div[6]/div[2]/a')))
            # Клик по кнопке
            btn_plus.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        "Кликаем по кнопке 'Удалить - Х'"
        try:
            # Ожидание, пока кнопка "X" станет кликабельной
            wait = WebDriverWait(self.browser, 10)  # Таймаут в 10 секунд
            btn_del = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div[1]/div[1]/div[6]/div[2]/div/div[2]/div/div[1]/div[2]/div[1]/button')))
            # Клик по кнопке
            btn_del.click()
        except Exception as e:
            print(f"Произошла ошибка: {e}")

        item_count = self.get_item_count()
        self.count_prods = item_count
