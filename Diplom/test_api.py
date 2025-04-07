import allure
import requests
import pytest


API_URL = "https://kinopoiskapiunofficial.tech/api"  



@allure.epic("Сайт Кинопоиск") 
@allure.severity("blocker")
@allure.title("API - тесты на сайт Кинопоиск")
@allure.description("В этом тест задании тестируется возможности поиска фильма, получение деталей о фильме, получение списка топовых фильмов а также получения отзыва")
@allure.feature("Проверка работы сайта")


def test_api_status():
   
    """Проверка статуса API"""
    response = requests.get(API_URL)
    assert response.status_code == 200

def test_api_movie_search():
    """Проверка поиска фильмов по запросу"""
    
    response = requests.get(API_URL + "movies/search", params={"query": "Матрица"})
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0 

def test_api_movie_details():
    """Проверка получения деталей фильма по ID"""
    movie_id = 301 
    response = requests.get(API_URL + f"movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert "title" in data  

def test_api_top_movies():
    """Проверка получения списка топ фильмов"""
    
    response = requests.get(API_URL + "movies/top")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) > 0  

def test_api_movie_reviews():
    """Проверка получения отзывов о фильме"""
    
    movie_id = 301  
    response = requests.get(API_URL + f"movies/{movie_id}/reviews")
    assert response.status_code == 200
    data = response.json()
    assert "reviews" in data  
    assert len(data["reviews"]) >= 0  


