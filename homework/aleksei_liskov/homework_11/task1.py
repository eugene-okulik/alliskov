class Book:
    material = 'Бумага'
    has_any_text = True

    def __init__(self, title, author, number_of_pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def info(self):
        print(self)

    def __str__(self):
        if self.is_reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'Страниц: {self.number_of_pages}, Материал: {Book.material}, Зарезервирована'
                    )
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'Страниц: {self.number_of_pages}, Материал: {Book.material}'
                    )


class SchoolBook(Book):

    def __init__(self, title, author, number_of_pages, isbn, is_reserved, subject, grade, has_exercises):
        super().__init__(title, author, number_of_pages, isbn, is_reserved)
        self.subject = subject
        self.grade = grade
        self.has_exercises = has_exercises

    def info(self):
        print(self)

    def __str__(self):
        if self.is_reserved:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'Страниц: {self.number_of_pages}, Предмет: {self.subject}, Класс: {self.grade}, Зарезервирована'
                    )
        else:
            return (f'Название: {self.title}, Автор: {self.author}, '
                    f'Страниц: {self.number_of_pages}, Предмет: {self.subject}, Класс: {self.grade}'
                    )


book_1 = Book('Властелин колец', 'Дж.Р.Р. Толкиен',
              1546, 9780007124015, False
              )

book_2 = Book('Идеальный шторм', 'Себастьян Джангер',
              248, 9780393337013, False
              )

book_3 = Book('Незнайка на луне', 'Николай Носов',
              488, 9785040930777, False
              )

book_4 = Book('Сказки братьев Гримм', 'Якоб Гримм, Вильгельм Гримм',
              272, 9781853261015, True
              )

book_5 = Book('Алиса в Стране Чудес', 'Льюис Кэрролл',
              272, 9781853261183, False
              )

school_book_1 = SchoolBook('Физика', 'Сидоренко', 301,
                           1111, False, 'Физика', 7, True)

school_book_2 = SchoolBook('Геометрия', 'Мамонтов', 432,
                           2222, False, 'Математика', 9, True)

school_book_3 = SchoolBook('Химия', 'Пятницкий', 135,
                           3333, True, 'Химия', 8, True)

book_1.info()
book_2.info()
book_3.info()
book_4.info()
book_5.info()

school_book_1.info()
school_book_2.info()
school_book_3.info()
