def year_control(user_year):
    year_c = user_year
    while year_c != '1799':
        print("Не верно")
        year_c = input('Ввведите год рождения А.С.Пушкина:')
    print('Верно')


def day_control(user_day):
    day_c = user_day
    while day_c != '6':
        print('Не верно!')
        day_c = input('Ввведите день рождения Пушкинa?')
    print('Верно')


year_control(input('Ввведите год рождения А.С.Пушкина:'))
day_control(input('Ввведите день рождения Пушкинa?'))
