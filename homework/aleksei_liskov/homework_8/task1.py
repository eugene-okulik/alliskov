import random

try:
    salary = int(input("Введите вашу зарплату: "))
    bonus = random.choice([True, False])
    if 0 >= salary:
        print("Введено число меньше или равное нулю")
    elif bonus:
        print("К зарплате будет добавлен бонус")
        print(f"Ваша зарплата с бонусом: {int(salary + salary * (random.randint(1,100)/100))}")
    else:
        print("К зарплате не будет добавлен бонус")
except ValueError:
    print("Для ввода необходимо использовать только целые числа без разделительных знаков")
