from file_data_receiver import read_data_from_csv
from db_data_receiver import find_student_by_attributes
from os import path

homework_dir = path.dirname(path.dirname(path.dirname(__file__)))
file_path = path.join(homework_dir, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

for line in read_data_from_csv(file_path):
    if find_student_by_attributes(
            line.get('name'),
            line.get('second_name'),
            line.get('group_title'),
            line.get('book_title'),
            line.get('subject_title'),
            line.get('lesson_title'),
            line.get('mark_value')
    ):
        print(f'В БД найдено совпадение по атрибутам: {line}')
    else:
        print(f'В БД не найдено совпадений по атрибутам: {line}')
