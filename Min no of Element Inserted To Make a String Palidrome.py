# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 04:34:28 2020

Problem Statement:Min no of Element Inserted To Make a String Palidrome

This Problem is same as min no of deletion to make a string palindrone. Hence,it
is also sub question of Longest Common Subsequent, but here we have to only find 
the longest palindromic subsequent. It can be done by finding longest palindromic 
subsequent in string and in its reverse subsequent.

Time Complexity: n**2

@author: RAVI
"""
def LCSubsequent(x,y,m):
    for i in range(m+1):
        for j in range(m+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][m]

def EleInserted():
    i=m
    j=m
    palin_str=[]
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            palin_str.insert(0,x[i-1])
            i-=1
            j-=1
        elif l[i][j-1]>l[i-1][j]:
            j-=1
        else:
            i-=1
    ans_str=list(x)
    for i in palin_str:
        if i in ans_str:
            ans_str.remove(i)
    ans_str="".join(ans_str)
    return ans_str
    





x=input("Insert string To be made pallindrome: ")
y=x[::-1]
m=len(x)
l=[[-1]*(m+1) for i in range(m+1)]
ans=m-LCSubsequent(x,y,m)
print(ans)
print(EleInserted())