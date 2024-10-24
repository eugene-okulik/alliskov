import os
from homework.aleksei_liskov.homework_13.services.date_service import DateService

if __name__ == '__main__':
    homework_directory_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    data_file_path = os.path.join(homework_directory_path, 'eugene_okulik', 'hw_13', 'data.txt')
    data_service = DateService()
    modified_items = data_service.modify_file(data_file_path)
    [print(item[1]) for item in modified_items]
