# -*- coding: utf-8 -*-
"""
Spyder Editor
Problem:Longest Common Subset
Time Complexity:n**2

This is a temporary script file.
"""
from prettytable import PrettyTable

def LCSubset(x,y,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=0
    max_len=0
                
    for i in range(m+1):
        for j in range(n+1):
            if max_len<l[i][j]:
                max_len=l[i][j]
                
    return max_len
                
    
def PrintSubset(ans):
    for i in range(m+1):
        for j in range(n+1):
            if l[i][j]==ans:
                req_i=i
                req_j=j
                
    subset=[]
    while ans!=0:
        if x[req_i-1]==y[req_j-1]:
            subset.insert(0,x[req_i-1])
            req_i-=1
            req_j-=1
            ans-=1
    
    return subset


x=input("Enter First String:")
y=input("Enter Second Sting:")
m=len(x)
n=len(y)
l=[[-1]*(n+1) for i in range(m+1)]
ans=LCSubset(x,y,m,n)
print(ans)    

Table=PrettyTable()
Table.field_names=[i for i in range(n+1)]
for i in l:
    Table.add_row(i)
    
print(Table)

subset=PrintSubset(ans)
print(subset)
