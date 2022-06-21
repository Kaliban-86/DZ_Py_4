def year_control(user_year):
    year_c = user_year
    while year_c != '1799':
        print("Не верно")
        year_c = input('Ввведите год рождения А.С.Пушкина:')
    print('Верно')

year = input('Ввведите год рождения А.С.Пушкина:')
year_control(year)