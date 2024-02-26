import json


def test_file_writer():
    data = {
        "vacancy_title": "Ведущий програмист-разработчик Unity, C#",
        "town": "Москва",
        "salary_from": 120000,
        "salary_to": 250000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/93159478"
    }

    with open('vacancies.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    with open('vacancies.json', 'r', encoding='utf-8') as file:
        saved_data = json.load(file)

    assert saved_data == {
        "vacancy_title": "Ведущий програмист-разработчик Unity, C#",
        "town": "Москва",
        "salary_from": 120000,
        "salary_to": 250000,
        "employment": "Полная занятость",
        "url": "https://hh.ru/vacancy/93159478"
    }
