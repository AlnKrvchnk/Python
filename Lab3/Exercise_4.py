'''
Напишите простой класс StringFormatter для форматирования строк со
следующим функционалом:
– удаление всех слов из строки, длина которых меньше n букв;
– замена всех цифр в строке на знак «*»;
– вставка по одному пробелу между всеми символами в строке;
– сортировка слов по размеру;
– сортировка слов в лексикографическом порядке.
'''

class StribngFormatter:
    def __init__(self,string):
        self.string=string
    def delword(self,n):
        self.string=(' '.join([word if len(word)>=n and word.isalpha() else ''.join([w for w in word if not(w.isalpha())]) for word in self.string.split(" ")]))
        return ' '.join([word if len(word)>=n and word.isalpha() else ''.join([w for w in word if not(w.isalpha())]) for word in self.string.split(" ")])
    def change(self):
        self.string=(''.join([words if not (words.isdigit()) else '*' for words in self.string]))
        return ''.join([words if not (words.isdigit()) else '*' for words in self.string])
    def space(self):
        self.string=(' '.join([w for w in self.string]))
        return ' '.join([w for w in self.string])
    def sortbylen(self):
        self.string=(' '.join(sorted([w for w in (''.join([word for word in self.string if word.isalpha() or word.isspace()])).split(' ') if (w.isalpha())],key=len)))
        return ' '.join(sorted([w for w in (''.join([word for word in self.string if word.isalpha() or word.isspace()])).split(' ') if (w.isalpha())],key=len))
    def sort(self):
        self.string=(' '.join(sorted([w for w in (''.join([word for word in self.string if word.isalpha() or word.isspace()])).split(' ') if (w.isalpha())])))
        return ' '.join(sorted([w for w in (''.join([word for word in self.string if word.isalpha() or word.isspace()])).split(' ') if (w.isalpha())]))

        


