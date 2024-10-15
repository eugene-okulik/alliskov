# Вариант с указанием количества повторений в аргументе функции
def decorate(func):
    def wrapper(text, number):
        for x in range(number):
            func(text, number)
    return wrapper


@decorate
def print_text(text, number):
    print(text)


print_text('Hello', 3)


# Вариант с указанием количества повторений в декораторе
def repeat(number):
    def decorate(func):
        def wrapper(text):
            for x in range(number):
                func(text)
        return wrapper
    return decorate


@repeat(3)
def print_text(text):
    print(text)


print_text('Bye')
