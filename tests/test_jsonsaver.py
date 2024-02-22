import pytest
from src.jsonsaver import JSONCSaver


@pytest.fixture
def json_saver():
    return JSONCSaver()


def test_file_writer():
    assert {
        "vacancy_title": "Ведущий програмист-разработчик Unity, C#",
        "town": "Москва",
        "salary_from": 120000,
        "salary_to": 250000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/93159478"
    }


def test_file_reader():
    assert {
        "vacancy_title": "Ведущий програмист-разработчик Unity, C#",
        "town": "Москва",
        "salary_from": 120000,
        "salary_to": 250000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/93159478"
    }