words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def multiple_print(**kwargs):
    for i in kwargs.items():
        text, number = i
        print(text * number)


multiple_print(**words)
