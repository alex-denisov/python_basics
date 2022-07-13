"""
2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user_info(name, l_name, birth, city, email, phone):
    """Вывод данных о пользователе в одну строку"""
    print(f'{name} {l_name} {birth} года рождения, '
          f'проживает в городе {city}, \nemail: {email}, телефон: {phone}')


user_info(
    name=input('Введите имя: '),
    l_name=input('Введите фамилию: '),
    birth=input('Введите год рождения: '),
    city=input('Введите ваш город: '),
    email=input('Введите ваш email: '),
    phone=input('Введите ваш телефон:')
)
