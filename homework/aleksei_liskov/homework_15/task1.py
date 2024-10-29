import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)
cursor = db.cursor(dictionary=True)

# Добавление студента
add_student_query = '''
insert into students (name, second_name, group_id) 
values (%s, %s, %s);
'''

cursor.execute(add_student_query, ('Robert', 'Horry', None))
student_id = cursor.lastrowid

# Добавление книг
add_book_query = '''
insert into books (title, taken_by_student_id)
values (%s, %s);
'''

cursor.executemany(
    add_book_query, [
        ('The Great Gatsby', student_id),
        ('Fahrenheit 451', student_id),
        ('Brave New World', student_id),
    ]
)

# Добавление группы
add_group_query = '''
insert into `groups` (title, start_date, end_date)
values (%s, %s, %s);
'''

cursor.execute(add_group_query, ('Group Of One', 2020, 2030))
group_id = cursor.lastrowid

# Закрепление студента в группе
update_student_group_query = '''
update students
set group_id = %s
where id = %s;
'''

cursor.execute(update_student_group_query, (group_id, student_id))

# Добавление учебных предметов
add_subject_query = '''
insert into subjets (title)
values (%s);
'''

subjects = ['Handmade', 'Ball Games', 'Musical Instruments']
subject_ids = {}
for subject in subjects:
    cursor.execute(
        add_subject_query, [subject]
    )
    subject_ids[subject] = cursor.lastrowid

# Добавление занятий по предметам
add_lesson_query = '''
insert into lessons (title, subject_id)
values (%s, %s);
'''

lessons = ['Knitting', 'Cooking', 'Volleyball', 'Soccer', 'Violin', 'Guitar']
lesson_ids = {}
for lesson in lessons:
    if lesson in [lessons[0], lessons[1]]:
        cursor.execute(
            add_lesson_query, (lesson, subject_ids.get(subjects[0]))
        )
    elif lesson in [lessons[2], lessons[3]]:
        cursor.execute(
            add_lesson_query, (lesson, subject_ids.get(subjects[1]))
        )
    elif lesson in [lessons[4], lessons[5]]:
        cursor.execute(
            add_lesson_query, (lesson, subject_ids.get(subjects[2]))
        )
    lesson_ids[lesson] = cursor.lastrowid

# Добавление студенту оценок по занятиям
add_mark_query = '''
insert into marks (value, lesson_id, student_id)
values (%s, %s, %s);
'''

cursor.executemany(
    add_mark_query, [
        (2, lesson_ids.get(lessons[0]), student_id),
        (4, lesson_ids.get(lessons[1]), student_id),
        (3, lesson_ids.get(lessons[2]), student_id),
        (3, lesson_ids.get(lessons[3]), student_id),
        (1, lesson_ids.get(lessons[4]), student_id),
        (5, lesson_ids.get(lessons[5]), student_id)
    ]
)

# Получить все оценки студента
get_student_marks_query = '''
select * from marks m
where m.student_id = %s;
'''

cursor.execute(get_student_marks_query, (student_id,))
student_marks = cursor.fetchall()
print(student_marks)

# Получить все книги, находящиеся у студента
get_student_books_query = '''
select * from books b
where b.taken_by_student_id = %s;
'''

cursor.execute(get_student_books_query, (student_id,))
student_books = cursor.fetchall()
print(student_books)

# Получить всю информацию о студенте
get_student_info_query = '''
select s.name, s.second_name,
b.title, g.title,
m.value, l.title, s2.title
from students s
join books b on b.taken_by_student_id = s.id
join `groups` g on g.id = s.group_id
join marks m on m.student_id = s.id
join lessons l on l.id = m.lesson_id
join subjets s2 on s2.id = l.subject_id
where s.id = %s
'''

cursor.execute(get_student_info_query, (student_id,))
student_info = cursor.fetchall()
print(student_info)

db.commit()
db.close()
