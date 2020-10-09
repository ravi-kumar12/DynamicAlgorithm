# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:43:59 2020
Evaluate Expression To True
    Given an expression, A, with operands and operators (OR , AND , XOR), in how
    many ways can you evaluate the expression to true, by grouping in different
    ways?
    Operands are only true and false.
    
Asked in:  
Amazon

Time Complexity:n**3
@author: RAVI
"""
def CountingWays(s,i,j,isTrue):
    if isTrue:
        temp=0
    else:
        temp=1
        
    if l[i][j][temp]!=-1:
        return l[i][j][temp]
    
    else:
        if i>j:
            return 0
        if i==j:
            if s[i]=="T" and isTrue==True:
                l[i][j][temp]=1
                return 1
            elif s[i]=="F" and isTrue==False:
                l[i][j][temp]=1
                return 1
            else:
                l[i][j][temp]=0
                return 0
        ans=0
        for k in range(i+1,j,2):
            Left_True=CountingWays(s,i,k-1,True)
            Left_False=CountingWays(s,i,k-1,False)
            Right_True=CountingWays(s,k+1,j,True)
            Right_False=CountingWays(s,k+1,j,False)
        
            if isTrue: 
                if s[k]=="|":
                    ans+=(Left_True*Right_True)+(Left_False*Right_True)+(Left_True*Right_False)
                elif s[k]=="&":
                    ans+=(Left_True*Right_True)
                else:
                    ans+=(Left_False*Right_True)+(Left_True*Right_False)
            else:
                if s[k]=="|":
                    ans+=(Left_False*Right_False)
                elif s[k]=="&":
                    ans+=(Left_True*Right_False)+(Left_False*Right_True)+(Left_False*Right_False)
                else:
                    ans+=(Left_False*Right_False)+(Left_True*Right_True)
                 
            
    
    l[i][j][temp]=ans        
    return ans
                
    
    
    
    
s=input("Enter Expression:")
n=len(s)
l=[[[-1]*2 for j in range(n)] for i in range(n)]

ans=CountingWays(s,0,n-1,True)
print(ans)