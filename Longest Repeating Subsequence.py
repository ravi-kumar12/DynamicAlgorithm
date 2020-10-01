# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:30:16 2020
# =============================================================================
# Longest Repeating Subsequence
# Problem:The longest repeated subsequence (LRS) problem is the problem of
#     finding the longest subsequences of a string that occurs at least twice.
#     The problem differs from problem of finding common substrings. Unlike 
#     substrings, subsequences are not required to occupy consecutive positions
#     within the original sequences.
# Time Complexity: n*2
# =============================================================================
@author: RAVI
"""
from prettytable import PrettyTable

def LRSubsequence(x,m,n):
    if l[m][n]!=-1:
        return l[m][n]
    else:
        
        if m==0 or n==0:
            l[m][n]=0
            return l[m][n]
        
        elif x[m-1]==x[n-1] and m!=n:
            l[m][n]=LRSubsequence(x,m-1,n-1)+1
            return l[m][n]
        
        else:
            l[m][n]=max(LRSubsequence(x,m-1,n),LRSubsequence(x,m,n-1))
            return l[m][n]
        
def PrintRepeatingSubsequence():
    i=m
    j=n
    res=''
    while i>0 and j>0:
        if x[i-1]==x[j-1] and i!=j:
            res+=x[i-1]
            i-=1
            j-=1
        elif l[i-1][j]>l[i][j-1]:
            i-=1
        else:
            j-=1
            
    return res[::-1]
    
    
x=input("Enter String:")
m=len(x)
n=m
l=[[-1]*(m+1) for i in range(n+1) ]

ans=LRSubsequence(x,m,n)
print(ans)

z=PrettyTable()
z.fieldnames =[i for i in range(m)]
for i in l:
    z.add_row(i)


print(z)

ans_str=PrintRepeatingSubsequence()
print(ans_str)


















