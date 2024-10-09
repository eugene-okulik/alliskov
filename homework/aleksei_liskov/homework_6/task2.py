numbers = range(1, 101)

for number in numbers:
    if number % 3 == 0:
        if number % 5 == 0:
            print('FuzzBuzz')
        else:
            print('Fuzz')
    elif number % 5 == 0:
        print('Buzz')
    else:
        print(number)
