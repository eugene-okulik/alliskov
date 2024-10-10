# Если результат возвращается в несколько строк (хотя и для отдельных строк тоже работает, просто лишняя логика будет)
text = ('результат операции: 42 \n'
        'результат операции: 54 \n'
        'результат работы программы: 209 \n'
        'результат: 2')


def print_increased_operation_result(i):
    results = i.split('\n')
    for item in results:
        increased_result = int((item.split())[-1]) + 10
        print(increased_result)


print_increased_operation_result(text)

# # Только если результат возвращается по одной строке
# text1 = 'результат операции: 42'
# text2 = 'результат операции: 54'
# text3 = 'результат работы программы: 209'
# text4 = 'результат: 2'
#
#
# def print_increased_operation_result(i):
#     increased_result = int((i.split())[-1]) + 10
#     print(increased_result)
#
#
# print_increased_operation_result(text1)
# print_increased_operation_result(text2)
# print_increased_operation_result(text3)
# print_increased_operation_result(text4)
