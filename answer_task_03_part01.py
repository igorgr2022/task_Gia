# Написать модуль, который реализует сравнение строк одним из рассмотренных в лекции методом.
# Написать в модуле конструкцию:
# if __name__ == '__main__'
# в котором провести проверку работы модуля, например как в лекции - парами строк.
# Написать программу, которая перебирает все элементы списка (задан в программе)
#  с некоторой строковой константой (также задана).

my_list = [('калоша', 'ладоши'), ('миру', 'мир'),('самовар', 'чайник'),('грипп', 
'гриб'),('молоко', 'молоток'), ('наша', 'каша'), ('Маша', 'Саша')]

def compare(S1, S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))

if __name__ == '__main__':
    for s, t in  my_list:
        print(s, t, compare(s, t))

print('======= поиск  строковой константы =========')

def iterating_over_a_string_constant():
    str_a = 'аша'
    for s, t in  my_list:
        if s.find('аша') == 1:
            print(s)
        if t.find(str_a) ==1:
            print(t)
iterating_over_a_string_constant()