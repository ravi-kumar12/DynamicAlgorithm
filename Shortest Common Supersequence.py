# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 11:00:48 2020
# =============================================================================
# SORTEST COMMON SUPERSEQUENCE:
#    PROBLEM STATEMENT:The shortest common supersequence of two sequences X and Y
#       is the shortest sequence which has X and Y as subsequences. This is a problem
#       closely related to the longest common subsequence problem. ... For the general
#       case of an arbitrary number of input sequences, the problem is NP-hard.
#       
#    Time Complexity:n**2
# =============================================================================
@author: RAVI
"""
from prettytable import PrettyTable
def LCSubsequence(x,y,m,n):
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j] = 0
            elif x[i-1]==y[j-1]:
                l[i][j] = l[i-1][j-1]+1
            else:
                l[i][j] = max(l[i-1][j],l[i][j-1])
                
    return l[m][n]
    
    
    
def SCSupersequence(x,y,m,n):
    return m+n-LCSubsequence(x,y,m,n)

def PrintSCSupersequence():
    i=m
    j=n
    subset=[]
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            subset.insert(0,x[i-1])
            i-=1
            j-=1
        elif l[i-1][j]<l[i][j-1]:
            subset.insert(0,y[j-1])
            j-=1
        else:
            subset.insert(0,x[i-1])
            i-=1
            
    if i!=0:
        subset.insert(0,x[:i])
        
    if j!=0:
        subset.insert(0,y[:j])
        
    subset=''.join(subset)
    
    return subset
            

x=input("Enter 1st String:")
y=input("Enter 2nd String:")

m=len(x)
n=len(y)

l=[[-1]*(n+1) for i in range(m+1)]

ans=SCSupersequence(x,y,m,n)

print(ans)


z=PrettyTable()
z.field_names=[i for i in range(n+1)]
for i in l:
    z.add_row(i)
    
print(z)


ans_lst=PrintSCSupersequence()
print(ans_lst)