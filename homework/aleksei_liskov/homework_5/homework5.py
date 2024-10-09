dividing_line = '=' * 40

# Задание 1
person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(dividing_line)
print(name, last_name, city, phone, country)

# Задание 2
result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"

# Вариант 1
result_1_number = int((result_1[result_1.index(":") + 1:]).strip()) + 10
result_2_number = int((result_2[result_2.index(":") + 1:]).strip()) + 10
result_3_number = int((result_3[result_3.index(":") + 1:]).strip()) + 10
print(dividing_line)
print(result_1_number)
print(result_2_number)
print(result_3_number)


# Вариант 2
def extract_number_from_result(result):
    start_index = result.index(":") + 1
    result_number = int((result[start_index:]).strip())
    final_number = result_number + 10
    return final_number


print(dividing_line)
print(extract_number_from_result(result_1))
print(extract_number_from_result(result_2))
print(extract_number_from_result(result_3))

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

# Вариант 1
print(dividing_line)
print(f"Students {', '.join(students)} study these subjects: {', '.join(subjects)}")

# Вариант 2
students = ', '.join(students)
subjects = ', '.join(subjects)
print('Students {0} study these subjects: {1}'.format(students, subjects))
