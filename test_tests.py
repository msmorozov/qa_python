from main import BooksCollector
import data
import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[1])

        # проверяем, что добавилось именно две
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize(
        'book_name, expected_books_count',
        [
            ('valid_name', 1),  # Пример валидного имени
            ('1', 1),  # Пример другого валидного имени
            ('123456789012345678901234567890123456789', 1),  # Имя длиной 39 символ
            ('1234567890123456789012345678901234567890', 1),  # Имя длиной 40 символов
        ]
    )
    def test_add_new_book_checking_valid_book_name(self, book_name, expected_books_count):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу с тестовым именем
        collector.add_new_book(book_name)

        #осуществляем проверку
        assert len(collector.get_books_genre()) == expected_books_count

        @pytest.mark.parametrize(
            'book_name, expected_books_count',
            [
                ('', 0),  # Пустая строка, если это допустимо
                ('12345678901234567890123456789012345678901', 0),  # Имя длиной 41 символов
            ]
        )
        def test_add_new_book_checking_unvalid_book_name(self, book_name, expected_books_count):
            # создаем экземпляр (объект) класса BooksCollector
            collector = BooksCollector()

            # добавляем книгу с тестовым именем
            collector.add_new_book(book_name)

            # осуществляем проверку
            assert len(collector.get_books_genre()) == expected_books_count

    def test_add_new_book_add_two_identical_book(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две одинаковых книги
        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[0])

        # проверяем, что добавилась одна из них
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 1
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_for_new_books(self, genre_detectives):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.set_book_genre(data.books[0], genre_detectives)
        actual_genre = collector.get_books_genre()

        # проверяем, полученный словарь жанров
        assert actual_genre == {data.books[0]: genre_detectives}

    def test_get_book_genre_correct_genre_for_the_book_is_returned(self, genre_detectives):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу
        collector.add_new_book(data.books[0])
        # устанавливаем добавленной книге существующий жанр
        collector.set_book_genre(data.books[0],genre_detectives)

        # проверяем, что в списоке books_genre есть добавленная книга с существующим жанром
        actual_genre = collector.get_book_genre(data.books[0])

        # ожидаемое значение
        expected_genre = genre_detectives

        assert actual_genre == expected_genre

    @pytest.mark.parametrize(
        'book_name_1, book_name_2, books_genre',
        [
            ('Гордость и предубеждение и зомби', 'Шерлок', 'Детективы'),
            ('Что делать, если ваш кот хочет вас убить', 'Вампиры', 'Ужасы'),
            ('Приключения Горка и Морка', 'Супермен', 'Фантастика'),
            ('Кот в сандалях', 'Операция Ы', 'Комедии'),
            ('Собачка Мяв', 'Колобок', 'Мультфильмы'),
        ]
    )
    def test_get_books_with_specific_genre_exists(self, book_name_1, book_name_2, books_genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу и жанр
        collector.add_new_book(book_name_1)
        collector.set_book_genre(book_name_1, books_genre)

        collector.add_new_book(book_name_2)
        collector.set_book_genre(book_name_2, books_genre)

        expected_name = collector.get_books_with_specific_genre(books_genre)
        # проверяем, вывод названий книг по жанрам
        assert expected_name == [book_name_1, book_name_2]

    @pytest.mark.parametrize(
        'book_name, books_genre',
        [
            ('Гордость и предубеждение и зомби', 'Детективы'),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы'),
            ('Приключения Горка и Морка', 'Фантастика'),
            ('Кот в сандалях', 'Комедии'),
            ('Собачка Мяв', 'Мультфильмы'),
        ]
    )
    def test_get_books_genre_for_books(self, book_name, books_genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем новую книгу и жанр
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, books_genre)

        actual_genre = collector.get_books_genre()

        # проверяем, полученный словарь жанров
        assert actual_genre == {book_name: books_genre}

    @pytest.mark.parametrize(
        'book_name, book_genre,expected_books_count',
        [
            ('Гордость и предубеждение и зомби', 'Детективы',0),
            ('Что делать, если ваш кот хочет вас убить', 'Ужасы',0),
            ('Приключения Горка и Морка', 'Фантастика',1),
            ('Кот в сандалях', 'Комедии',1),
            ('Собачка Мяв', 'Мультфильмы',1),
        ]
    )
    def test_get_books_for_children_show_count_books_with_age_rayting(self, book_name, book_genre, expected_books_count):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name,book_genre)

        expected_books = collector.get_books_for_children()

        assert len(expected_books) == expected_books_count

    def test_get_books_for_children_show_name_books_without_age_rayting(self, genre_detectives,genre_fantastic,
                                                                     genre_сartoons):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.set_book_genre(data.books[0],genre_detectives)

        collector.add_new_book(data.books[2])
        collector.set_book_genre(data.books[2], genre_fantastic)

        collector.add_new_book(data.books[3])
        collector.set_book_genre(data.books[3], genre_сartoons)

        expected_books = collector.get_books_for_children()

        assert expected_books == [data.books[2], data.books[3]]

    def test_add_book_in_favorites_and_show_them(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[2])

        collector.add_book_in_favorites(data.books[2])
        favorites_books = collector.get_list_of_favorites_books()

        assert favorites_books == [data.books[2]]

    def test_add_book_in_favorites_and_show_non_existent_book(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[2])

        collector.add_book_in_favorites('Не существующая книга')
        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 0

    def test_add_book_in_favorites_twice(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[2])

        collector.add_book_in_favorites(data.books[2])
        collector.add_book_in_favorites(data.books[2])
        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[2])

        collector.add_book_in_favorites(data.books[0])
        collector.add_book_in_favorites(data.books[2])

        collector.delete_book_from_favorites(data.books[2])
        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 1
        assert favorites_books == [data.books[0]]

    def test_delete_book_from_favorites_non_existent_book(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_book_in_favorites(data.books[0])

        collector.delete_book_from_favorites('Не существующая книга')
        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 1

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book(data.books[0])
        collector.add_new_book(data.books[1])

        collector.add_book_in_favorites(data.books[0])
        collector.add_book_in_favorites(data.books[1])

        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 2

    def test_get_list_of_favorites_books_empty(self):
        collector = BooksCollector()

        favorites_books = collector.get_list_of_favorites_books()

        assert len(favorites_books) == 0