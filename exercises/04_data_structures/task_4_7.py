# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"
abc = mac.split(':')
#a = int((abc[0]),16)
#b = int((abc[1]),16)
#c = int((abc[-1]),16)
abc = ''.join(abc)
print(abc) 
#abc = (bin(a)+bin(b)+bin(c))
#abc = abc.split('0b')
#print(abc[1]+abc[2]+abc[-1])

abc1 = bin(int(abc,16))
print(abc1[2:])

