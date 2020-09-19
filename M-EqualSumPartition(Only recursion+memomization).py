def SubSetSum(arr,n,s):
    global l
    if l[n][s]!=None:
        return l[n][s]
    if n==0 and s!=0:
        l[n][s]=False
        return False
    elif n!=0 and s==0:
        l[n][s]=True
        return True
    elif n==0 and s==0:
        l[n][s]=True
        return True
    elif arr[n-1]<=s:
        l[n][s]= (SubSetSum(arr,n-1,s-arr[n-1]) or SubSetSum(arr,n-1,s))
        return (SubSetSum(arr,n-1,s-arr[n-1]) or SubSetSum(arr,n-1,s))
    else:
        l[n][s]=SubSetSum(arr,n-1,s)
        return SubSetSum(arr,n-1,s)


def MEqualSumPartition(n,arr,m,req_arrays):
    global l
    if sum(arr)==0 and m==0:
        return True
    
    elif sum(arr)%m!=0:
        return False
    else:
        l=[[None]*((sum(arr)//m)+1) for i in range(n+1)]
        res=SubSetSum(arr,n,sum(arr)//m)
        if res==False:
            return False
        if res:
            i=n
            s=sum(arr)//m
            j=s
            lst1=[]
            while s!=0:
                while i>1 and l[i][j]==l[i-1][j]:
                    i-=1
                lst1.insert(0,arr[i-1])
                s-=arr[i-1]
                i-=1
                j=s
            req_arrays.append((lst1))
            print(lst1,m)
            for i in lst1:
                arr.remove(i)
            return True and MEqualSumPartition(n-len(lst1),arr,m-1,req_arrays)
                
n=11#int(input("Enter No of Element:"))
arr=[1,2,3,4,5,5,6,7,8,9,10]#sorted(list(map(int,input("Enter Element:").split(" "))))
m=5#int(input("no of subset to get:"))
req_arrays=[]  
ans=MEqualSumPartition(n,arr,m,req_arrays)
print(ans)
if ans:
    for i in req_arrays:
        print(i)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        