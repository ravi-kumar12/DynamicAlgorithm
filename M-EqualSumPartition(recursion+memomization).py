def EqualSumPartition(n,arr,m):
    global l
    counter=0
    while len(arr)!=0 and m!=0:
        if sum(arr)%m!=0:
            return False
        else:
            s=sum(arr)//m
            l=[[None]*(s+1) for i in range(n+1)]
            res=SubSetSum(arr,n,s)
            if res and sum(arr)!=s:
                i=n
                j=s
                lst1=[]
                while s!=0:
                    while i>1 and l[i][j]==l[i-1][j]:
                        i-=1
                    lst1.insert(0,arr[i-1])
                    s-=arr[i-1]
                    i-=1
                    j=s
                print(lst1)
                for i in lst1:
                    arr.remove(i)
                n=n-len(lst1)
                m=m-1
            if res and sum(arr)==s:
                 print(arr)
                 counter=1
                 break
    if counter==1:
        return True
                   

def SubSetSum(arr,n,s):
    global l
    if l[n][s]!=None:
        return l[n][s]
    elif n==0 and s!=0:
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
    


n=15#int(input("Enter No of Element:"))
arr=[1,2,3,4,5,6,7,8,9,10,11,6,7,8,9]#list(map(int,input("Enter Element").split(" ")))
m=6
ans=EqualSumPartition(n,arr,m)
print(ans)