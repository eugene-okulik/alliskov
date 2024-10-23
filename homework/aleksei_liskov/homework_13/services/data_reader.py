from datetime import datetime
from homework.aleksei_liskov.homework_13.models.file_item import FileItem


class DataReader:
    def _read_file(self, file_path) -> list[str]:
        with open(file_path, 'r', encoding='utf8') as data_file:
            data = data_file.readlines()
        return data

    def read_items(self, file_path) -> list[FileItem]:
        lines = self._read_file(file_path)
        items = []
        for line in lines:
            row_num = int(line[0:line.index('. ')])
            date_str = line[line.index('. ')+2:line.index(' - ')]
            date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S.%f')
            action = line[line.index(' - ')+3:len(line)]
            item = FileItem(row_num, date, action)
            items.append(item)
        return items
