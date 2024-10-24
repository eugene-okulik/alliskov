import datetime
from homework.aleksei_liskov.homework_13.services.data_reader import DataReader

week_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


class DateService:

    def __init__(self):
        self._data_reader = DataReader()

    def modify_file(self, file_path) -> list:
        items = self._data_reader.read_items(file_path)
        modified_items = []
        for item in items:
            if item.row_num == 1:
                result = item.date + datetime.timedelta(weeks=1)
                comment = f'Измененная дата: {result}'
            elif item.row_num == 2:
                result = datetime.datetime.isoweekday(item.date)
                comment = f'День недели в указанной дате: {week_days[result]}'
            elif item.row_num == 3:
                result = (datetime.datetime.now() - item.date).days
                comment = f'Количество дней с указанной даты до текущей: {result}'
            modified_items.append((result, comment))
        return modified_items
