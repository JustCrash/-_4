from src.utils import user_choice_hh


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """
    print('Здравтсвуйте. \n'
          'Эта программа поможет вам в поиске вакансии на сайте: Headhunter. \n'
          'Введите да или нет. \n'
          'Да - Запустить программу. \n'
          'Нет - Закрыть программу. \n')

    while True:
        user_choice_platform = input()
        if user_choice_platform == 'да':
            print('HeadHunter')
            user_choice_hh()
            break
        elif user_choice_platform == 'нет':
            print('До встречи!')
            break
        else:
            print('Неверный запрос.')
            break


if __name__ == '__main__':
    user_interaction()
