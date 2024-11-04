import argparse
from log_file_analyzer import LogFileAnalyzer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Программа выполнит поиск по файлам в выбранной директории'
                    ' и отобразит совпадения по искомому слову')

    parser.add_argument('--path',
                        type=str,
                        help='Полный путь к директории с логами')
    parser.add_argument('--keyword',
                        type=str,
                        help='Искомое слово')
    parser.add_argument('--context',
                        type=int,
                        default=5,
                        help='Количество отображаемых слов до и после искомого слова. По умолчанию 5')
    parser.add_argument('--show_all',
                        action='store_true',
                        help='Показать все найденные совпадения. По умолчанию только первое')

    args = parser.parse_args()

    parsed_file = LogFileAnalyzer().find_in_file(file_path=args.path,
                                                 keyword=args.keyword,
                                                 context_words_number=args.context,
                                                 show_all=args.show_all)

    found, filename, line_number, result = next(parsed_file)

    if not found:
        print(result)
    elif args.show_all:
        for found, filename, line_number, result in parsed_file:
            print(f'Совпадение в файле {filename} - строка {line_number}: {result}')
    else:
        print(f'Совпадение в файле {filename} - строка {line_number}: {result}')
