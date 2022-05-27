import statistics
# Сумму ряда 0 - 88888888
my_list =[]
for i in range(1, 88888889):
    my_list.append(i)
print("Сумму ряда 0 - 88888888: ",sum(my_list))

# Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
avg = statistics.mean ([3, 4, 56, 100, 2, 2, 3])
print("Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]: ", avg)
    
# Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
my_str_1 = "asdxfghyxyx"
my_str_2=""
for j in my_str_1:
    if j=='x':
        j='y'
    my_str_2 +=j
my_str_1 = my_str_2
print('Заменить в строке "asdxfghyxyx" все буквы "х" на "у": ', my_str_1)

# Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], 
# кратных и 3 и 5.
list_a = [3, 4, 56, 100, 15, 2, 20, 30]
num_a=1
for k in list_a:
    if k%3==0 and k%5 ==0:
        num_a*=k
print('Произведение кратных и 3 и 5:  ', num_a)

#  Заменить все буквы "х" на "у" в исходной строке 
#  без использования дополнительной строки.
my_str = "asdxfghyxyx"
my_str = my_str.replace('x', 'y')
print('Замена в строке "asdxfghyxyx"  букв "х" на "у"\nбез использования дополнительной строки:   ', my_str)
