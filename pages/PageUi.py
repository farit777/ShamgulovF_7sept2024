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


    @allure.step("Проверка доступности стран по ссылке")
    def open_countries(self):
        """Открывает страницу стран"""
        countries_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/9/']")
        countries_link.click()

    @allure.step("Проверка доступности Годы по ссылке")
    def open_years(self):
        """Открывает страницу Годы"""
        years_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/7/']")
        years_link.click()

    @allure.step("Проверка доступности Критика по ссылке")
    def open_critics(self):
        """Отрывает страницу отзывов"""
        critics_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/18/']")
        critics_link.click()

    @allure.step("Проверка сериалов на странице фильмов по ссылке")
    def open_incoming(self):
        """Открывает страницу поступлений за фильмы"""
        incoming_link = self.browser.find_element(By.CSS_SELECTOR, "a[href='/lists/categories/movies/5/']")
        incoming_link.click()


    # @allure.step("Закрыть модальное окно, если оно открыто")
    # def close_modal_if_open(self):
    #     """Функция закрывает модальное окно, если оно присутствует"""
    #     try:
    #         modal_close_button = self.browser.find_element(By.CSS_SELECTOR, "body > div.ReactModalPortal > div > div > div > div:nth-child(1) > div.styles_buttonContainer__R98ro > button.style_button__PNtXT.style_buttonSize48__7RF4w.style_secondaryTransparent__ehaDu.style_buttonDark__beFpy.style_fullWidth__Kw7rX")
    #         modal_close_button.click()
    #     except Exception as e:
    #         allure.attach(self.browser.get_screenshot_as_png(), name="Modal Close Error", attachment_type=allure.attachment_type.PNG)
    #         print("Модальное окно не найдено или не открыто.")