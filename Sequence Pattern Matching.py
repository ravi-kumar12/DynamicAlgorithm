# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 00:02:23 2020
# =============================================================================
# Sequence Pattern Matching:
# Problem Statement:Find that string x is subsequence of y or not
# This Problem is sub problem of longest common subsequent.
# =============================================================================
@author: RAVI
"""


def LCSubsequence():
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j]=0
            elif x[i-1]==y[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    return l[m][n]
                

x=input("Enter Seq To Find:")
y=input("Enter String in which we have to FInd:")
m=len(x)
n=len(y)
l=[[-1]*(n+1) for i in range(m+1)]

if len(x)==LCSubsequence():
    print(True)
else:
    print(False)