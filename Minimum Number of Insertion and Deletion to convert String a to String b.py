# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:57:09 2020
Minimum Number of Insertion and Deletion to convert String a to String b
Time Complexity:n**2
@author: RAVI
"""

def LCSubset(x,y,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=1+l[i-1][j-1]
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    max_len=0
                
    for i in range(m+1):
        for j in range(n+1):
            if max_len<l[i][j]:
                max_len=l[i][j]
                
    return max_len
                
        
    
    
    
x=input("Enter String To Convert:")
y=input("Enter String To get:")

m=len(x)
n=len(y)

l=[[-1]*(n+1) for i in range(m+1)]

lcs=LCSubset(x,y,m,n)


ans=(m+n-2*lcs)             #(m-lsd)+(n-lcs)
print(ans)