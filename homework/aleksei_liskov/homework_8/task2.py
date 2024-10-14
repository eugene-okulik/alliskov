def fibonacci_sequence():
    fibonacci_row = [0, 1]
    counter = 2
    while 1 == 1:
        fibonacci_row = (fibonacci_row[-1], fibonacci_row[-1] + fibonacci_row[-2])
        counter += 1
        yield fibonacci_row[-1], counter


for number, position in fibonacci_sequence():
    if position == 5:
        print(f"Пятое число Фибоначчи: {number}")
    elif position == 200:
        print(f"Двухсотое число Фибоначчи: {number}")
    elif position == 1000:
        print(f"Тысячное число Фибоначчи: {number}")
    elif position == 100000:
        print(f"Стотысячное число Фибоначчи: {number}")
        break
