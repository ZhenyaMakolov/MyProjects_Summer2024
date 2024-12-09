# программа, которая принимает на вход текущие дату и время и определяет, сколько времени осталось до выхода курса

from datetime import datetime

def choose_plural(amount, declensions):
    if str(amount).endswith(('5', '6', '7', '8', '9', '0', '11', '12', '13', '14')):
        res = f'{amount} {declensions[2]}'
    elif str(amount).endswith(('2', '3', '4')):
        res = f'{amount} {declensions[1]}'
    else:
        res = f'{amount} {declensions[0]}'
    return res

mask = '%d.%m.%Y %H:%M'
declensions = [
    ['день', 'дня', 'дней'],
    ['час', 'часа', 'часов'],
    ['минута', 'минуты', 'минут']
]
premiere = datetime.strptime('08.11.2022 12:00', mask)
present_date = datetime.strptime(input(), mask)
all_time = premiere - present_date

days = choose_plural(all_time.days, declensions[0])
hours = choose_plural(all_time.seconds // 3600, declensions[1])
if hours[1].isdigit():
    hours2 = hours[:2]
else:
    hours2 = hours[0]
minutes = choose_plural(all_time.seconds // 60 - int(hours2) * 60, declensions[2])
    
if present_date >= premiere:
    print('Курс уже вышел!')
else:
    res, count, result = 'До выхода курса осталось: ', 0, []
    for element in [days, hours, minutes]:
        if int(element[0]):
            result.append(element)
            count += 1
        if count == 2:
            break
    print(res, end='')
    print(*result, sep=' и ')