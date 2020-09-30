# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 18:43:45 2020
Problem:Find the longest common subset in two string.
Approach:
    without Dynamic
Time complexity:worse:n**2 if string have all any element in common.
                    and 
                best:n if string dont have any element in common.
@author: RAVI
"""

x=input()
y=input()

if len(x)>len(y):
    x,y=y,x
i=0
temp_y=y
max_ser=0

while i<len(x):
    counter=0
    
    try:
        j=temp_y.index(x[i])
        counter=1
    except:
        i+=1
        temp_y=y
    if counter==1:
        count=0
        temp_j=j
        temp_i=i
        
        ans=""
        while (i<len(x) and j<len(temp_y)) and x[i]==temp_y[j]:
            ans+=x[i]
            count+=1
            i+=1
            j+=1
            
        i=temp_i
        temp_y=temp_y[(temp_j+1):]
        if max_ser<count:
            max_ser=count
            ans_string=ans
print("{} is answer string with length {}.".format(ans_string,max_ser))            