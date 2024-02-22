import pytest
from src.vacancy import Vacancy
from abc import ABC
from src.abstacted_classes import GetVacancies
from src.hh_API import HeadHunterAPI


@pytest.fixture
def i():
    i = Vacancy("Ведущий програмист-разработчик Unity, C#",
                "Масква",
                "120000",
                "250000",
                "Полная занятость",
                "https://hh.ru/vacancy/93159478")
    return i


def test_issubclass():
    assert issubclass(GetVacancies, ABC)
    assert issubclass(HeadHunterAPI, GetVacancies)
