def simple_separator():
    return "**********"


print('first function result: ', simple_separator())


def long_separator(count):
    sep = ''
    for num in range(count):
        sep = sep + '*'
    return sep


print('second function result: ', long_separator(3))
print('second function result: ', long_separator(4))


def separator(simbol, count):
    sep = simbol
    for num in range(count):
        sep = sep + simbol
    return sep


print('third function result: ', separator('-', 10))
print('third function result: ', separator('#', 5))  # True


def hello_world():
    print('fourth function result:')
    print('**********')
    print('Hello World!')
    print('##########')


hello_world()


def hello_who(who='World'):
    print(f'Hellow {who}!')


print('fifth function result')
hello_who()
hello_who('Max')
hello_who('Kate')


def pow_many(power, *args):
    sum = 0
    for i in args:
        sum += i
    return sum ** power


print('sixth function result: ')
print(pow_many(1, 1, 2))
print(pow_many(1, 2, 3))
print(pow_many(2, 1, 1))
print(pow_many(3, 2))
print(pow_many(2, 1, 2, 3, 4))


def print_key_val(**kwargs):
    for k, v in kwargs.items():
        print(k, '-->', v)


print('seventh function result: ')
print_key_val(name='Max', age=21)
print_key_val(animal='Cat', is_animal=True)


def my_filter(iterable, function):
    return list(filter(function, iterable))

print('eighth function result: ')
print(my_filter([1, 2, 3, 4, 5], lambda x: x > 3))
print(my_filter([1, 2, 3, 4, 5], lambda x: x == 2))
print(my_filter([1, 2, 3, 4, 5], lambda x: x != 3))
print(my_filter(['a', 'b', 'c', 'd'], lambda x: x in 'abba'))
