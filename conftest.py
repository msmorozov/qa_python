import pytest


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