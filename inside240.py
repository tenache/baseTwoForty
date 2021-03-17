# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 15:28:36 2021

@author: Usuario
"""

def inside240(x):
    digits=[]
    if x==0:
        digits.append('0')
    else:
        factors=[120,80,60,48,40,30,24,20]
        charsUni=[937,438,397,606,662,546,580,1039]
        chars=[]
        for i in range(len(charsUni)):
            char=chr(charsUni[i])
            chars.append(char)
    
        a=0
        i=0
        
        
        while x >= 20:
            while a < 1:
                a= x / factors[i]
                i += 1
            x= x % factors[i - 1]
            digits.append(chars[i - 1]) 
            a=0

        if 0 < x < 10 :
            digits.append(str(x))
        elif x > 0:
            digits.append(chr(x + 55))
    values = " ".join(f"{v}" for v in digits)
    print(values)            
    return digits
 
    