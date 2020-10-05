# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 09:08:54 2020

@author: RAVI
"""
from sys import maxsize
from prettytable import PrettyTable

def MCM(arr,i,j):
    if l[i][j]!=-1:
        return l[i][j]
    else:
        if i>=j:
            l[i][j]=0
            parenthesis[i][j]=0            
            return 0
        else:
            min_ans=maxsize
            for k in range(i,j):#k goes from i to j-1
                temp_ans=MCM(arr,i,k)+MCM(arr,k+1,j)+arr[i-1]*arr[k]*arr[j]
                
                if temp_ans<min_ans:
                    min_ans=temp_ans
                    parenthesis[i][j]=k
    l[i][j]=min_ans
    return min_ans

def printop(i,j):
    if i==j:
        print("A{}".format(i),end="")
    else:
        print("(",end="")
        printop(i,parenthesis[i][j])
        printop(parenthesis[i][j]+1,j)
        print(")",end="")
        
    

    
        
        
                
    
arr=list(map(int,input("Enter Array Representing Matrix Dimension: ").split(" ")))
n=len(arr)
l=[[-1]*(n) for i in range(n)]
parenthesis=[[-1]*(n) for i in range(n)]#for printing multiplication way
ans=MCM(arr,1,n-1)

print(ans)
    
y=PrettyTable()
y.field_names=[i for i in range(n)]
for i in parenthesis:
    y.add_row(i)
    
print(y)

printop(1,n-1)