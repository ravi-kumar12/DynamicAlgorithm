# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:31:47 2020

Problem Statement
        LCS Problem Statement: Given two sequences, find the length of longest 
        subsequence present in both of them. A subsequence is a sequence that
        appears in the same relative order, but not necessarily contiguous.
Time Complexity-n**2       

@author: RAVI
"""
from prettytable import PrettyTable

def LCS():
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]
                

def TableCreation():
    x=PrettyTable()
    x.field_names=[i for i in range(n+1)]   
    for i in range(m+1):
        x.add_row(l[i])
    return x

def Eleadded():
    i=m
    j=n
    ans_str=""
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            ans_str+=y[j-1]
            i-=1
            j-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
             
    return ans_str[::-1]


x=input("Enter First String:")
y=input("Enter second String:")
m=len(x)
n=len(y)
l=[[-1]*(n+1) for i in range(m+1)]

ans=LCS()
print(ans)

Table=TableCreation()
print(Table)

print(Eleadded())
