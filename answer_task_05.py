# Программа напоминалка о днях рождения
import datetime

birthdays = {
    '07072007': 'Петрова Игоря Сергеевича',
    '08072007': 'Субботина Николая Дмитриевича',
    '09072007': 'Безпамятных Дмитрия Сергеевича',
    '21072007': 'Аполинария Вячеслава Игоревича',
    '24072007': 'Зварич Алесея Германовича',
     }

current_date = str(datetime.datetime.today())                                    #получаем текущую дату
current_year= int(current_date[:4])                                              #текущий год
current_day_month= current_date[8:10] + current_date[5:7]                        #текущий день и месяц


for a, b in birthdays.items():
    key_d_m = a[:4]                                                              #день и месяц в ключе
    key_y = int(a[4:8])                                                          #год в ключе
    if key_d_m == current_day_month:                                             #если совпала дата в ключе с текущей датой
        x = current_year - key_y                                                 #разность текущего года и найденного
        print(x, 'годовщина', b)
    for z in range(1, 16):
        changed_date= str(datetime.datetime.today() + datetime.timedelta(days=z))#добавляем к текущей дате n дней
        changed_day_month = changed_date[8:10] + changed_date[5:7]               #измененная на n дней дата
        changed_year= int(current_date[:4])                                      #изменненный на n дней год
        if key_d_m == changed_day_month:                                         #если совпала дата в ключе с измененной датой
            anniversary = changed_year - key_y                                   #разность текущего года и найденного
            print('До ', anniversary, 'годовщины ', b, ' осталось', z, 'дней' )

#С pep8 код выглядит довольно привклекательнее и читательнее. Я за pep8.