def choose_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return f'{first} + {second} = {first + second}'
    elif operation == '-':
        return f'{first} - {second} = {first - second}'
    elif operation == '*':
        return f'{first} * {second} = {first * second}'
    elif operation == '/':
        return f'{first} / {second} = {first / second}'


first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))


print(calc(first, second))
