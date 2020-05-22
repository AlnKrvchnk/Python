import re
import os
import hashlib
import subprocess
import math


'''                                                    Ex1'''
'''Напишите скрипт, который читает текстовый файл и выводит символы
в порядке убывания частоты встречаемости в тексте. Регистр символа
не имеет значения. Программа должна учитывать только буквенные
символы'''

def funk(dic, i):
    dic [i]+=1
    
def ex1():
    dic={}
    with open("Ex1.txt") as file:
        t=file.read()
    file.close()
    text=[i.lower() for i in t]        
    d={ funk(dic, i)  if i in dic else dic.update({i:1}) for i in text if  i.isalpha()}
    list=[sorted(dic.items(), key=lambda x: -x[1])]
    print(list)

'''                                                           Ex2'''
'''Напишите скрипт, позволяющий искать в заданной директории и в ее
подпапках файлы-дубликаты на основе сравнения контрольных сумм
(MD5). Файлы могут иметь одинаковое содержимое, но отличаться
именами. Скрипт должен вывести группы имен обнаруженных файловдубликатов. '''

def read(path,dict,rez):
    list=os.listdir(path)    # списочек из фаликов в папочке path
    for i in list:
        path_file=str(path)+'\\'+str(i)
        if os.path.isdir(str(path_file)):
            list_=[]
            read(path_file,dict,rez)
        else:
            with open(path_file) as file :
                hash_object = hashlib.md5((file.read()).encode())
                if hash_object.hexdigest() in dict:
                    if hash_object.hexdigest() in rez:
                        rez[hash_object.hexdigest()].append(i)
                    else:
                        d=str(dict[hash_object.hexdigest()])
                        rez[hash_object.hexdigest()]=[d,i]
                else:
                    dict.update({hash_object.hexdigest():i}) #hash -kay, i - value
    file.close()
    return rez
     
    
def ex2():
    dict={}
    rez={}
    path=str(input('Введите директорию:'))
    read(path,dict,rez)
    j=1
    for key in rez:
        print('Группа '+str(j)+':')
        for i in rez[key]:
            print(i)
        j+=1
'''                                                           Ex3'''
'''     Задан путь к директории с музыкальными файлами (в названии
которых нет номеров, а только названия песен) и текстовый файл,
хранящий полный список песен с номерами и названиями в виде строк
формата «01. Freefall [6:12]». Напишите скрипт, который корректирует
имена файлов в директории на основе текста списка песен.'''

def ex3():
    path_audio="C:\\Users\\Алина\\Desktop\\Python\\Lab2\\Музыка"
    path_text="Ex3.txt"
    list=os.listdir(path_audio)
    pattern=r'^\d+\.\s.+\s\[\d{1,2}\:\d\d\]$'
    for i in list:   #i-название муз. файла
        with open(path_text,encoding="utf8") as  file:
            for line in file:
                if line.find(i[0:-4])!=-1:
                    if re.search(pattern,line):
                        line=line.replace("\n", i[-4:])
                        os.rename(path_audio+"\\"+i,path_audio+"\\"+line)
                        
'''                                                           Ex4'''
'''     Вариант 5: найдите все номера телефонов – подстроки вида
«(000)1112233» или «(000)111-22-33»'''

def ex4():
    path=str(input('Введите название файла:'))
    with open(path,encoding="utf8") as file:
        l=1
        for line in file:
            for m in re.finditer(r'\(\d{3}\)\d{3}\-?\d\d\-?\d\d', line):
                print('Строка {line}, позиция {pos} : найдено \'{m}\','.format(line=l,pos=m.start(),m=m.group())) 
            l+=1
            
'''                                                           Ex5'''
'''     Введите с клавиатуры текст. Программно найдите в нем и выведите
отдельно все слова, которые начинаются с большого латинского
символа (от A до Z) и заканчиваются 2 или 4 цифрами, например
«Petr93», «Johnny70», «Service2002». Используйте регулярные
выражения.'''       
    
def ex5():
    text=str(input('Введите текст:'))
    pattern=r'\b([A-Z][a-z]*\d{2}|[A-Z][a-z]*\d{4})\b'
    word=re.findall(pattern,text)
    print(word )


'''                                                           Ex6'''
'''     Напишите скрипт reorganize.py, который в директории --source создает
две директории: Archive и Small. В первую директорию помещаются
файлы с датой изменения, отличающейся от текущей даты на
количество дней более параметра --days (т.е. относительно старые
файлы). Во вторую – все файлы размером меньше параметра --size байт.
Каждая директория должна создаваться только в случае, если найден
хотя бы один файл, который должен быть в нее помещен. Пример
вызова:
 reorganize --source "C:\TestDir" --days 2 --size 4096'''    
def ex6():
    t=subprocess.call("reorganize.py --source \"C:\\Users\\Алина\\Desktop\\Python\\Lab2\"--days 2 --size 4096",shell=True)
'''                                                       Ex7'''
'''Написать скрипт trackmix.py, который формирует обзорный трек-микс альбома
(попурри из коротких фрагментов mp3-файлов в пользовательской директории).
Для манипуляций со звуковыми файлами можно использовать сторонние утилиты, например, FFmpeg.
Пример вызова и работы скрипта: trackmix --source "C:\Muz\Album" --count 5 --frame 15 -l -e --- processing file 1: 01 - Intro.mp3 --- processing file 2: 02 - Outro.mp3 --- done!
'''
def ex7():
     t=subprocess.call("trackmix.py -s \"C:\\Users\\Алина\\Desktop\\Python\\Lab2\" -d \"kek.mp3\" -f 15 -l --extended",shell=True)
switcher={
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7:ex7}
selected_ex=10
while selected_ex!=0:
    try:
       selected_ex=int(input("Выберите задание (1-7, 0-выход):"))
       if 0<selected_ex<8:
          switcher.get(selected_ex)()
       elif selected_ex==0:
          selected_ex=0
    except Exception:
       print("Фи")
