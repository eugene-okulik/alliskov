def add_text(func):

    def wrapper(text):
        func(text)
        print("Finished")
    return wrapper


@add_text
def print_text(text):
    print(text)


print_text('Hello')
    