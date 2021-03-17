# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 11:51:11 2021

@author: Usuario
"""



def newSystem(x):
    digitList=[]
    i=0
    dig0=241
    while dig0 >= 240:
        expo=240**i
        dig0=int(x / expo)
        i += 1
    digitList.append(dig0)
    rest=x % expo
    i -=1
    while i >= 1:
        i -= 1
        digN=int(rest/ (240 ** i))
        digitList.append(digN)
        rest= x % (240 ** i)
    return digitList


   