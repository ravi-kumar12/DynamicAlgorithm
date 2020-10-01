# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 20:21:52 2020
# =============================================================================
# Minimum number of deletion in a string to make it a palindrome:
# =============================================================================

@author: RAVI
"""

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
y=x[::-1]
m=len(x)
n=m
l=[[-1]*(n+1) for i in range(m+1)]

ans=m-LCS()
print(ans)

ans_str=Eleadded()
print(ans_str)