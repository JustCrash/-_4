import pytest
from src.vacancy import Vacancy


@pytest.fixture
def i():
    i = Vacancy("Ведущий програмист-разработчик Unity, C#",
                "Москва",
                120000,
                250000,
                "Полная занятость",
                "https://hh.ru/vacancy/93159478")
    return i


def test__init__(i):
    assert i.vacancy_title == "Ведущий програмист-разработчик Unity, C#"
    assert i.town == "Москва"
    assert i.salary_from == 120000
    assert i.salary_to == 250000
    assert i.employment == "Полная занятость"
    assert i.url == "https://hh.ru/vacancy/93159478"
