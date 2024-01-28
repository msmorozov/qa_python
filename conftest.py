import pytest


# Названия книг
@pytest.fixture
def first_book():
    return 'Гордость и предубеждение и зомби'

@pytest.fixture
def second_book():
    return 'Что делать, если ваш кот хочет вас убить'

@pytest.fixture
def third_book():
    return 'Приключения Горка и Морка'

@pytest.fixture
def fourth_book():
    return 'Собачка Мяв'

# Жанры книг
@pytest.fixture
def genre_detectives():
    return 'Детективы'

@pytest.fixture
def genre_horror():
    return 'Ужасы'
@pytest.fixture
def genre_fantastic():
    return 'Фантастика'

@pytest.fixture
def genre_сartoons():
    return 'Мультфильмы'