import random

random_number = random.randint(1, 10)
user_number = 0

while user_number != random_number:
    try:
        user_number = int(input("Угадайте число от 1 до 10: "))
        if 11 > user_number > 0:
            if user_number != random_number:
                print("Не угадали. Попробуйте снова")
                continue
            elif user_number == random_number:
                print("Поздравляю! Вы угадали!")
                break
        else:
            print("Введено число вне диапазона от 1 до 10. Попробуйте снова")
            continue
    except ValueError:
        print("Пожалуйста, введите целое число от 1 до 10")
