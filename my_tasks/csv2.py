# программа читает файл (пассажиры титаника)
# выводит количество выживших пассажиров моложе 18 лет

import csv

with open('titanic.csv', encoding='utf-8') as f:  # чтение файла
    res = list(csv.reader(f, delimiter=';'))
    del res[0]
    res2 = list(filter(lambda x: x[0] == '1' and float(x[3]) < 18, res))  # отбор выживших младше 18 лет
    [print(i[1]) for i in filter(lambda x: x[2] == 'male', res2)]  # отбор мальчиков
    [print(j[1]) for j in filter(lambda x: x[2] == 'female', res2)]  # отбор девочек