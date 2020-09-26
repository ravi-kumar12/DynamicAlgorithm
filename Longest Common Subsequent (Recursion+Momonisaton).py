# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 08:13:36 2020

Problem Statement
        LCS Problem Statement: Given two sequences, find the length of longest 
        subsequence present in both of them. A subsequence is a sequence that
        appears in the same relative order, but not necessarily contiguous.
Time Complexity-n**2       

@author: RAVI
"""
from prettytable import PrettyTable

def LCS(x,y,m,n):
    if l[m][n]!=-1:
        return l[m][n]
    else:
        if m==0 or n==0:
            l[m][n]=0
            
        elif x[m-1]==y[n-1]:
            l[m][n]=1+LCS(x,y,m-1,n-1)
           
        else:
            l[m][n]=max(LCS(x,y,m-1,n),LCS(x,y,m,n-1))
        return l[m][n]
        
def TableCreation():
    x=PrettyTable()
    x.field_names=[i for i in range(n+1)]   
    for i in range(m+1):
        x.add_row(l[i])
    return x

def elementadded():
    count=l[m][n]
    ans_str=""
    j=n
    i=m
    while count!=0:
        while l[i][j]==l[i][j-1]:
            j-=1
        ans_str+=y[j-1]
        i-=1
        j-=1
        count-=1
       
            
    return ans_str[::-1]

x=input("Enter First String:")
y=input("Enter second String:")
m=len(x)
n=len(y)
l=[[-1]*(n+1) for i in range(m+1)]

ans=LCS(x,y,m,n)
print(ans)

Table=TableCreation()
print(Table)

print(elementadded())