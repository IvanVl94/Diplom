import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


BASE_URL = "https://www.kinopoisk.ru/"



@allure.epic("Сайт Кинопоиск") 
@allure.severity("blocker")
@allure.title("UI - тесты на сайт Кинопоиск")
@allure.description("В этом тест задании тестируется, корректная работа сайта, поиск фильмов, навигация по разделу, нахождение информации о фильме, а также проверяет наличие полей для ввода логина и пароля ")
@allure.feature("Проверка работы сайта")


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_homepage_title(browser):
    """Проверка заголовка главной страницы"""
   
    browser.get(BASE_URL)
    assert "КиноПоиск" in browser.title

def test_search_functionality(browser):
    """Проверка функциональности поиска"""
   
    browser.get(BASE_URL)
    search_box = browser.find_element(By.NAME, "kp_query")
    search_box.send_keys("Матрица")                        # Поиск фильм "Матрица"
    search_box.send_keys(Keys.RETURN)
    assert "Тест" in browser.title

def test_navigation_to_movies(browser):
    """Проверка навигации к разделу 'Фильмы'"""
    
    browser.get(BASE_URL)
    movies_link = browser.find_element(By.CLASS_NAME, "styles_root__7mPJN styles_lightThemeItem__BSbZW" )
    movies_link.click()
    assert "Фильмы" in browser.title

def test_movie_details(browser):
    """Проверка перехода на страницу деталей фильма"""
    
    browser.get(BASE_URL)
    movie_link = browser.find_element(By.XPATH, "//a[contains(@href, '/film/')]")
    movie_link.click()
    assert "Фильм" in browser.title

def test_user_login_page(browser):
    """Проверка доступности страницы входа пользователя"""
    browser.get(BASE_URL + "user/login/")
    assert "Вход" in browser.title
    assert browser.find_element(By.NAME, "login")  # Вести свой логин
    assert browser.find_element(By.NAME, "password") # Вести свой пароль 

browser.quit()