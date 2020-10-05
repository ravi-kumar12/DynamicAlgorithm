# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 05:34:03 2020

MATRIX CHAIN MULTIPLICATION:
    Definition: Given a sequence of matrices such that any matrix may be multiplied
    by the previous matrix, find the best association such that the result is obtained
    with the minimum number of arithmetic operations. One may use dynamic programming
    to find the best association.
    
Time Complexity: O(n**3)
    
    
@author: RAVI
"""
from sys import maxsize
def MCM():
    for i in range(n):
        mul[i][i]=0
        br[i][i]=0
                
                
    for d in range(1,n):
        for i in range(n-d):
            j=i+d
            ans=maxsize
            for k in range(i,j):
                temp_ans=mul[i][k]+mul[k+1][j]+arr[i-1]*arr[k]*arr[j]
                if  temp_ans<ans:
                    ans=temp_ans
                    br[i][j]=k
                    mul[i][j]=ans
                    
    print(mul[1][n-1])
    
                
def eleadd(i,j):
    if i==j:
        print("A{}".format(i),end="")
    else:
        print("(",end="")
        eleadd(i,br[i][j])
        eleadd(br[i][j]+1,j)
        print(")",end="")
    
    
    
    
    
    
    
    
arr=[2,3,4,5,6]#input("Enter Dimension:")
n=len(arr)
mul=[[-1] *(n) for i in range(n)]                   #no of mul
br=[[-1] *(n) for i in range(n)]                    #no
MCM()
eleadd(1,n-1)