# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from inside240 import inside240
from newSystem import newSystem
from base240 import base240

def main():
    
    numberString=input('Print any number and try to figure out this system ')
    
    print('type q or Q to quit ')
    
    while numberString != 'Q' and numberString !='q':
        x=int(numberString)
        base240(x)
        numberString=input('Number: ')
        
    messages=[]
    messages.append('Always enter to continue')
    messages.append('You can also try base240(yourNumber) in your terminal')
    messages.append('Every DIGIT can be stored in a list element')
    messages.append('For example, DIGITS=base240(yourNumber)')
    messages.append('Every digit may be several symbols, so look out')
    enter=''
    i=0
    while enter=='' and i in range(len(messages)):
        print(messages[i])
        enter=input('Next ')
        i += 1
        
    
    messages2=[]
    messages2.append('When the number is bigger than 240, I just print every digit on a different line')
    messages2.append('You may want to separate them by comma or not print them at all')
    messages2.append('Just type base240(yourNumber,False)')
    messages2.append('This will not print out your number')
    messages2.append('Now I will print out all numbers from 1 to 20')
    i=0
    while enter=='' and i in range(len(messages2)):
        print(messages2[i])
        enter=input('Next ')
        i += 1
        
    oneToTwenty=[]
    for i in range(21):
        oneToTwenty.append(base240(i,False)[0][0])
        values = " ".join(f"{v}" for v in oneToTwenty)
    print(values)
        
    enter=input('Continue printing all factors of 240, except 240 (press Enter)')
    
    factors=[1,2,3,4,5,6,8,10,12,15,16,20,24,30,40,60,80,120]
    factorsOfTwoForty=[]
    for i in factors:
        factorsOfTwoForty.append(base240(i,False)[0][0])
        values = " ".join(f"{v}" for v in factorsOfTwoForty)
    print(values)    
        
if __name__ == "__main__":
    main()






    
