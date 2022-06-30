my_list = [('калоша', 'ладоши'), ('миру', 'мир'),('самовар', 'чайник'),('грипп', 
'гриб'),('молоко', 'молоток'), ('наша', 'каша'), ('Маша', 'Саша')]



class String_comparison:
    def compare(self, S1, S2):
        ngrams = [S1[i:i+3] for i in range(len(S1))]
        count = 0
        for ngram in ngrams:
            count += S2.count(ngram)
        return count / max(len(S1), len(S2))

if __name__ == '__main__':
    str_01 = String_comparison()
    for s, t in  my_list:
        print(s, t, str_01.compare(s, t))