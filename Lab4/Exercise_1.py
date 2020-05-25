'''Напишите скрипт, читающий во всех mp3-файлах указанной
директории ID3v1-теги и выводящий информацию о каждом файле в
виде: [имя исполнителя] - [название трека] - [название альбома].
Если пользователь при вызове скрипта задает ключ -d, то выведите
для каждого файла также 16-ричный дамп тега. Скрипт должен
также автоматически проставить номера треков и жанр (номер
жанра задается в параметре командной строки), если они не
проставлены. Используйте модуль struct.
ID3v1-заголовки располагаются в последних 128 байтах mp3-файла. '''

import argparse
from struct import*
import os


parser = argparse.ArgumentParser()
parser.add_argument('-d')
my_parser = parser.parse_args()

path= os.getcwd()+'\\Audio'
pathSongs=os.listdir(path)


for i in pathSongs:
     with open(path+'\\'+i, 'rb') as file:
          file.seek(-128,2)
          f=file.read()
          teg,track,artist,albom,number=unpack('<3s30s30s30s35s',f)
          print('['+ artist.decode('windows-1251') + " ]  -  [ " +track.decode('windows-1251') + " ]  -  [ " + albom.decode('windows-1251') + " ]")
               
               
     
