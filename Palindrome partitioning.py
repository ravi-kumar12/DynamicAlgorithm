# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:59:11 2020
Palindrome partitioning
    Problem: Find the min no of partition such that each sub string obtained is
    palindrone.
    Given a string, a partitioning of the string is a palindrome partitioning if
    every substring of the partition is a palindrome. ... If a string is a 
    palindrome, then minimum 0 cuts are needed. If a string of length n containing
    all different characters, then minimum n-1 cuts are needed.
    
    Based on Matrix Chain Multiplication

    Time Complexity-n**3
@author: RAVI
"""
from sys import maxsize
from prettytable import PrettyTable

def isPalindrome(s,i,j):
    if i==j:
        return True
    st=s[i:j+1]
    n=len(st)
    
    for i in range(n//2):
        if st[i]!=st[n-i-1]:
            return False
    return True
    


def PalindromePartitioning(s,i,j):
    if l[i][j]!=-1:
        return l[i][j]
    else:
        if isPalindrome(s,i,j) or i>=j:
            l[i][j]=0
            return l[i][j]
        final_res=maxsize
        for k in range(i,j):
            left=PalindromePartitioning(s,i,k)   #more optizition
            right=PalindromePartitioning(s,k+1,j)
            res=left+right+1
            if res<final_res:
                final_res=res
                k_values[i][j]=k
        l[i][j]=final_res
        return l[i][j]

def printingString(s,i,j):
    if isPalindrome(s,i,j):
        print(s[i:j+1])
    else:
        printingString(s,i,k_values[i][j])
        printingString(s,k_values[i][j]+1,j)
    

s=input("Enter String:")
n=len(s)
l=[[-1]*(n) for i in range(n)]
k_values=[[-1]*(n) for i in range(n)]
ans=PalindromePartitioning(s,0,n-1)
print(ans)

x=PrettyTable()
x.field_names=[i for i in range(n)]
for i in k_values:
    x.add_row(i)
print(x)

printingString(s,0,n-1)



