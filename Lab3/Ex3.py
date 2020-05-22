import os
import re

def read (path):
      list=[]
      with open(path,encoding="utf8") as file:
            l=1
            for line in file:
                  for m in re.finditer(r'\(\d{3}\)\d{3}\-?\d\d\-?\d\d', line):
                        list.append('Строка {line}, позиция {pos} : найдено \'{m}\',\n'.format(line=l,pos=m.start(),m=m.group()))
                  l+=1
      return (list)
            
