# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:48:37 2019

@author: PC
"""

dic={'0001':'A','0010':'B','0011':'C','0000':'D','0100':'E','1111':'F','0101':'G','1001':'H'}
c=input()
a_list=[]
b_list=[]
for i in range(0,len(c),4):
    code=c[i:i+4]
    a_list.append(code)
for every in a_list:
    if every in dic:
        b_list.append(dic[every])       
    else: 
       b_list=['Not Found!']
       break
for j in b_list:
    print(j,end='')
