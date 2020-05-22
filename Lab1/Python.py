from array import *
from decimal import Decimal
#                                                            №1
#              Напишите скрипт, который преобразует введенное с клавиатуры
#                                  вещественное число в денежный формат.
                                                        
def ex1():
   try :
      a=Decimal(input("Введите число:"))
      if a>-1:
          a_int=Decimal(str(int(a)))
          a_double=a-a_int
          a_double*=100
          a_double=int(a_double)
          print(str(a_int)+".руб "+str(a_double)+".коп ")
          
      else:
           print("Некорректный формат!")
   except Exception:
      print("Число в формате 00.00")

#                                                            №2
#               Написать скрипт, который выводит на экран «True», если элементы
#                   программно задаваемого списка представляют собой возрастающую
#                                       последовательность, иначе – «False».


def compare(list_compare):
   length=len(list_compare)-1
   while length!=1:
     if list_compare[length-1]>list_compare[length]:
        comp=False
        break
     if list_compare[length-1]<list_compare[length]:
        comp=True
     length-=1
   return comp

def ex2():
    list_1=[23,45,67,78,79,80]
    list_2=[34,12,67,45,34,89]
    
    comp_1=compare(list_1)
    comp_2=compare(list_2)
    print(bool(comp_1))
    print(bool(comp_2))

#                                                            №3
#              Напишите скрипт, который позволяет ввести с клавиатуры номер
#                   дебетовой карты (16 цифр) и выводит номер в скрытом виде

def ex3():
      while True:
          try :
               cod=str(int(input("Введите номер дебетовой карты (16 цифр):")))
               if(len(cod)!=16):
                       print("Неверное количество цифр!")
               else:
                    break
          except  ValueError:
               print("Неверный номер!")
      print(str(cod[0:4])+" **** **** "+str(cod[12:16]))
   

#                                                            №4
#           Напишите скрипт, который разделяет введенный с клавиатуры текст
#        на слова и выводит сначала те слова, длина которых превосходит 7 символов,
#        затем слова размером от 4 до 7 символов, затем – все остальные.

#dfdgfgdfg,dfgdfdf
def ex4():
   text=input("Введите текст:")
   text+=" "
   list=[]
   s=""
   for i in text:
       if (i==' 'or i==','or i=='-'or i=='.'):
           if (s!=''):
               list.append(s)
               s=""
       else:
           s+=i
   print(list)
   for i in list:
       if(len(i)>7):
           print(i)
           
   for i in list:
       if(3<len(i) and 8>len(i) ):
           print(i)
   for i in list:
       if(4>len(i) ):
           print(i)  

#                                                            №5
#        Напишите скрипт, который позволяет ввести с клавиатуры текст предложения и
#        сформировать новую строку на основе исходной, в которой все слова,
#        начинающиеся с большой буквы,
#        приведены к верхнему регистру. Слова могут разделяться запятыми или пробелами
def ex5():
   text=str(input("Введите текст:"))
   text=text.split(' ')
   text=[(str.upper()) if str.istitle() else str for str in text]
   text=' '.join(text)
   print(text)
   

#                                                            №6
 #       Напишите программу, позволяющую ввести с клавиатуры текст
 #       предложения и вывести на консоль все символы,
 #       которые входят в этот текст ровно по одному разу
    
def ex6():
   text=str(input("Введите текст:"))
   text=text.lower()
   size=int(len(text))
   text=[s for s in text if text.find(s,0,size)==text.rfind(s, 0,size)]
   print(text)

#                                                            №7
#            Напишите скрипт, который обрабатывает список строк-адресов следующим образом:
#             сначала определяет, начинается ли каждая строка в списке с префикса «www».
#           Если условие выполняется, то скрипт должен вставить  в начало этой строки префикс
#           «http://», а затем проверить, что строка заканчивается на «.com».
#            Если у строки другое окончание, то скрипт должен вставить в конец подстроку «.com».
    
def ex7():
   list=["www.gfhjkl.com","fghj","jhkl","www.fgh","ghjk.com","bnm,"]
   print(list)
   list=[("http://"+ str) if str.startswith("www.") else str for str in list ]
   print(list)
   list=[str if str.endswith(".com") else str+".com" for str in list ]
   print(list)


#                                                            №8
#        Напишите скрипт, генерирующий случайным образом число n в диапазоне от 1 до 10000.
#       Скрипт должен создать массив из n целых чисел, также сгенерированных случайным образом,
#         и дополнить массив нулями до размера, равного ближайшей сверху степени двойки.

import random
   
def Pow(n):
    pow =2
    a=2
    while a<n:
        a=2**pow
        pow+=1
    return a
   
def Rand():
   return random.randint(1, 1000)

def ex8():

   n=Rand()
   array=[0]*n
   i=0
   while i!=n:
       array[i]=Rand()
       i+=1
   k=Pow(n)-n
   array.extend([0]*k)
   
#                                                            №9
#        Выберите структуру данных для хранения купюр разного достоинства
#        в заданном количестве. При вводе пользователем запрашиваемой суммы денег,
#        скрипт должен вывести на консоль количество купюр подходящего достоинства. 

def Res(i,money,money_value,value,result,count):
    result_=0
    result_=int(money/money_value[int(value.get(i))])
    if result_>count[int(value.get(i))]:
        result[int(value.get(i-1))]=result_-count[int(value.get(i))]
        if i==1:
            return 0
        else:
            money=money-money_value[int(value.get(i))]*count[int(value.get(i))]
            Res(i-1,money,money_value,value,result,count)
        result[int(value.get(i))]=count[int(value.get(i))]
        count[int(value.get(i))]=0
    else:
        result[int(value.get(i))]=result_
        if i==1 or money==0:
            return result 
        else:
            money=money-(money_value[int(value.get(i))]*result[int(value.get(i))])
            Res(i-1,money,money_value,value,result,count)
    
def Sum(money,count):
    return int(sum([mon*coun for mon, coun in zip(money, count)]))
   
def ex9():
      money_value=[10,50,100,500,1000]
      count=[10 for i in money_value]
      sum=Sum(money_value,count)
      result=[0 for i in money_value]
      value={
          1:0,
          2:1,
          3:2,
          4:3,
          5:4 }

      flag=False
      while flag==False:
          try:
              money=int(input("Введите сумму:"))
          except ValueError:
              print("Введите сумму!")
          else:
              flag=True
          if money%10!=0:
                  print("Cумма не кратна 10!")
                  flag=False
          if money<0:
                  print("Сумма не может быть меньше 0!")
                  flag=False
          if money>sum:
                  print("Сумма привышает лимит банка!")
                  flag=False
      i=5
      Res(i,money,money_value,value,result,count)
      i-=1
      string=""
      while i>-1:
          if result[i]!=0:
              string+=str(result[i])+"*"+str(money_value[i])+"+"
          i-=1   
      string=string[:len(string)-1]
      print(string,'=',money)
    
     
#                                                            №10
#Напишите скрипт, позволяющий определить надежность вводимого
#пользователем пароля. Это задание является творческим:
#алгоритм определения надежности разработайте самостоятельно. 
def ex10():
   import re
   password=input("Введите пароль:")
   lvl=0
   if(re.search('\d+',password) is not None):
       lvl+=1
   if(re.search('\D+',password) is not None):
       lvl+=1
   if(re.search('\s+',password) is not None):
       lvl+=1
   if(len(password)>10):
        lvl+=1
   if(re.search('[A-Z]',password)is not None):
       lvl+=1
   if(re.search('[a-z]',password)is not None):
       lvl+=1

   print("Уровень"+str(lvl))
    
#                                                            №11
#     Напишите генератор frange как аналог range() с дробным шагом.

def frange(start,end,step):
    list_=[]
    step=Decimal(str(step))
    x=Decimal(str(start))
    while x<end:
        list_.append(float(x))
        x+=step
    yield list_
   
def ex11():
   for x in frange(1,3,0.2):
      print(x)
      
#                                                            №12
#    Напишите генератор get_frames(), который производит «оконную декомпозицию»
#  сигнала: на основе входного списка генерирует набор списков –
#  перекрывающихся отдельных фрагментов сигнала размера size
#  со степенью перекрытия overlap.

def get_frames(signal, size, overlap):
    size = size*overlap
    start = 0
    end = int(size)
    while end<=len(signal):
        frame = signal[start:end]
        yield frame
        start+=int(size)
        end += int(size)
def ex12():
      signal = [23, 45, 34, 56, 23, 334, 345, 234, 78, 23, 35, 325, 234, 7, 67, 463]
      for frame in get_frames (signal, size = 16, overlap = 0.25):
          print (frame)
          
#                                                            №13
# Напишите собственную версию генератора enumerate под названием extra_enumerate.

def extra_enumerate(x):
    size=sum(x)
    cum=0
    i=1
    for elem in x:
        cum+=elem
        frac=cum/size
        yield i,elem,cum,frac
        i+=1
    
def ex13():
      x=[2,6,8,4]
      for i, elem, cum, frac in extra_enumerate(x):    
          print(elem,cum,frac)
    
#                                                            №14
#     Напишите декоратор non_empty, который дополнительно
#     проверяет списковый результат любой функции:
#     если в нем содержатся пустые строки или значение None, то они удаляются
def decorator(func):
    def non_empty():
        a=func()
        #a = filter(None,func())
        a=[x for x in a if x]
        return a
    return non_empty
    
@decorator
def get_pages():   
    return ['chapter1', None, 'contents', '', 'line1']
   
def ex14():
      print(get_pages())
      
 #                                                            №15

def pre_process(a=0.97):
    def deckor(func):
        def wrapper(s):
            for i in range(len(s)):
                s[i] =s[i]- a * s[i - 1]
                print(s[i])
        return wrapper
    return deckor

@pre_process(a=0.93)
def plot_signal(s):
    for sample in s:
        print(sample)
def ex15():
      data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
      plot_signal(data)

#                                                            №16
#    Напишите скрипт, который на основе списка из 16 названий футбольных
#  команд случайным образом формирует 4 группы по 4 команды, а также выводит
#  на консоль календарь всех игр (игры должны проходить по средам, раз в 2
#  недели, начиная с 14 сентября текущего года). Даты игр необходимо выводить
#  в формате «14/09/2016, 22:45». Используйте модули random и itertools.  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
def ex16():
      from itertools import combinations
      import random
      import datetime
      teams=list(range(1,17))
      teams=[str(str(i)+" команда" )for i in teams]
      random.shuffle(teams)
      i=1
      j=0
      while j!=len(teams)-1:
        if j==0 or j==3 or j==7 or j==11:
          print("Группа №",i)
          i+=1
        print(teams[j])
        j+=1 
      groups_1=list(combinations([teams.pop(0) for x in range(4)],2))
      groups_2=list(combinations([teams.pop(0) for x in range(4)],2))
      groups_3=list(combinations([teams.pop(0) for x in range(4)],2))
      groups_4=list(combinations([teams.pop(0) for x in range(4)],2))
      print(groups_1)

      date_=datetime.datetime(2020,9,14,20,20)
      while date_.weekday()!=2:
          date_+=datetime.timedelta(days=1)
      i=0   
      while i<len(groups_1):
         a=date_.strftime("%d/%m/%Y, %H:%M")
         print(a,"\n",groups_1[i],"\n",groups_2[i],"\n",groups_3[i],"\n",groups_4[i] )
         date_+=datetime.timedelta(days=7)
         i+=1

switcher={
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7,
    8: ex8,
    9: ex9,
    10: ex10,
    11: ex11,
    12: ex12,
    13: ex13,
    14: ex14,
    15: ex15,
    16: ex16,
    }

selected_ex=20

while selected_ex!=0:
    try:
       selected_ex=int(input("Выберите задание (1-16, 0-выход):"))
       if 0<selected_ex<17:
          switcher.get(selected_ex)()
          
       elif selected_ex==0:
          selected_ex=0
    except Exception:
       print("Фи")


    
