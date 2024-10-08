import random

my_dict = (
    {'tuple': ('Green', 'Blue', 'Red', 'Yellow', 'Brown', 'Black', 'White'),
     'list': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
     'dict': {1: 'Atlantic', 2: 'Pacific', 3: 'Indian', 4: 'Arctic', 5: 'Antarctic'},
     'set': {10, 20, 30, 40, 60, 70, 80}
     }
)

dividing_line = "=" * 40
print(dividing_line)

# Вывести на экран последний элемент в tuple
print(f"Последний элемент в tuple: {my_dict['tuple'][-1]}")
print(dividing_line)

# Добавить в конец list еще один элемент
added_item = my_dict['list'].append('Tuesday')
print(f"В конец list добавлен элемент: {my_dict['list'][-1]}")

# Удалить из list второй элемент
deleted_list_item = my_dict['list'].pop(1)
print(f"Из list удален второй элемент: {deleted_list_item}")
print(dividing_line)

# Добавить в dict элемент с ключом ('i am a tuple',) и любым значением
new_dict_item_key = ('i am a tuple',)
my_dict['dict'][new_dict_item_key] = (1, 2, 3, 4, 5)
print(f"В dict добавлен элемент {new_dict_item_key}: {my_dict['dict'].get(new_dict_item_key)}")

# Удалить любой элемент из dict
random_dict_item_key = random.choice(list(my_dict['dict'].keys()))
deleted_dict_item_value = my_dict['dict'].pop(random_dict_item_key)
print(f"Из dict удален элемент {random_dict_item_key}: {deleted_dict_item_value}")
print(dividing_line)

# Добавить в set новый элемент
new_set_item = random.randint(100, 1000)
my_dict['set'].add(new_set_item)
print(f"В множество добавлен элемент {new_set_item}")

# Удалить любой элемент из set
random_set_item = random.choice(list(my_dict['set']))
my_dict['set'].remove(random_set_item)
print(f"Из множества удален элемент {random_set_item}")
print(dividing_line)

# Вывести на экран весь словарь
print(f"Содержимое словаря my_dict: \n {my_dict}")
