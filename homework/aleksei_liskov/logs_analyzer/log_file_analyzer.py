import os
import re


class LogFileAnalyzer:

    def find_in_file(self, file_path, keyword, context_words_number, show_all):
        found = 0
        for filename in os.listdir(file_path):
            with open(os.path.join(file_path, filename), 'r', encoding='utf8') as file:
                for count_line, line in enumerate(file, start=1):
                    parsed_line = re.findall(r'\b\w+\b', line)
                    for index, word in enumerate(parsed_line):
                        if keyword.lower() in word.lower():
                            found += 1
                            first_word = max(index - context_words_number, 0)
                            last_word = min(index + context_words_number + 1, len(parsed_line))
                            words_before = ' '.join(parsed_line[first_word:index])
                            words_after = ' '.join(parsed_line[index + 1:last_word])
                            final_string = f'{words_before} {word.upper()} {words_after}'
                            yield found, filename, count_line, final_string

                            if not show_all:
                                return
        if not found:
            yield 0, None, None, 'Совпадений не найдено'
