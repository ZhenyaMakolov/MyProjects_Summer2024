# Функция приводит содержимое файла в CSV формат, 
# сгруппировав строки по первому столбцу и назвав первый столбец id_name

import csv

def condense_csv(filename, id_name):
    with open(filename, encoding='utf-8') as f:
        res, headers, mydict = list(csv.reader(f)), [], {}
        for i in range(len(res)):
            mydict.setdefault(res[i][0], []).append(res[i][-1])  # добавление ключей и значений
            if res[i][1] not in headers:
                headers.append(res[i][1])  # создание заголовков

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as f2:  # запись файла
        res2 = csv.writer(f2)
        res2.writerow([id_name] + headers)
        for k, v in mydict.items():
            res2.writerow([k, *v])