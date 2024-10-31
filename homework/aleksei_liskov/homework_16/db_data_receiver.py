import mysql.connector as mysql
import dotenv
import os

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME'),
)

cursor = db.cursor()


def find_student_by_attributes(name, second_name, group_title, book_title, subject_title, lesson_title, mark_value):
    query = '''
    select count(1)
    from students s
    join books b on b.taken_by_student_id = s.id
    join `groups` g on g.id = s.group_id
    join marks m on m.student_id = s.id
    join lessons l on l.id = m.lesson_id 
    join subjets s2 on s2.id = l.subject_id
    where s.name = %s
    and s.second_name = %s
    and g.title = %s
    and b.title = %s
    and s2.title = %s
    and l.title = %s
    and m.value = %s;
    '''
    cursor.execute(query, (name, second_name, group_title, book_title, subject_title, lesson_title, mark_value))
    counter, = cursor.fetchone()
    return counter
