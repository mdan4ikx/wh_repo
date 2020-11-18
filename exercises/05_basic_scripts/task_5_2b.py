#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

ip = argv[1]
ip = ip.split('.')
ip1, ip2, ip3, ip4 = int(ip[0]), int(ip[1]), int(ip[2]), 0

mask = int(argv[2])
mask0 =('1' * mask + ((32-mask)*'0'))
mask1 = int(mask0[0:8], 2)
mask2 = int(mask0[8:16], 2)
mask3 = int(mask0[16:24], 2)
mask4 = int(mask0[24:32], 2)
acc_templ = (f'''
Network:
{ip1:<8}   {ip2:<8}   {ip3:<8}  {ip4:<8}
{ip1:08b}  {ip2:08b}  {ip3:08b} {ip4:08b}

Mask:
/{mask}
{mask1:<8} {mask2:<8} {mask3:<8} {mask4:<8}
{mask1:08b} {mask2:08b} {mask3:08b} {mask4:08b}''')


print(acc_templ.format(mask))
            


