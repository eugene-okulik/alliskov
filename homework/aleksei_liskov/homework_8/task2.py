def fibonacci_sequence(limit=100):
    fibonacci_row = [0, 1]
    count = len(fibonacci_row)
    while count < limit:
        fibonacci_row.append(fibonacci_row[-1] + fibonacci_row[-2])
        yield fibonacci_row
        count += 1


for items in fibonacci_sequence(200000000):
    if len(items) == 5:
        print(f"Пятый элемент в списке: {items[-1]}")
    elif len(items) == 200:
        print(f"Двухсотый элемент в списке: {items[-1]}")
    elif len(items) == 1000:
        print(f"Тысячный элемент в списке: {items[-1]}")
    elif len(items) == 100000:
        print(f"Стотысячный элемент в списке: {items[-1]}")
        break
