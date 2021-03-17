# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from inside240 import inside240
from newSystem import newSystem

def base240(x):
    Twofortydigits=[]
    digitList=newSystem(x)
    for i in range(len(digitList)):
        Twofortydigits.append(inside240(digitList[i]))
        # print(Twofortydigits[i]) 
    return Twofortydigits

    
