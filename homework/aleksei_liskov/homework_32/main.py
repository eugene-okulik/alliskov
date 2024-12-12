from datetime import datetime
from time import sleep

new_year_start = datetime.strptime("01-01-2025 00:00:00", '%d-%m-%Y %H:%M:%S')

while True:
    sleep(1)
    new_year_counter = str((new_year_start - datetime.now())).split()
    days = new_year_counter[0]
    time = new_year_counter[2].split('.')[0]
    print(f'New year in {days} days {time}')