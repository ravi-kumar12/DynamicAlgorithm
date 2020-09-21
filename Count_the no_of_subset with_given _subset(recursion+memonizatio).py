from prettytable import PrettyTable
def CountSubset(arr,n,s):
    if l[n][s]!=-1:
        return l[n][s]
    else:
        if n==0 and s!=0:
            l[n][s]=0
            return 0
        elif n!=0 and s==0:
            l[n][s]=1
            return 1
        elif n==0 and s==0:
            l[n][s]=1
            return 1
        elif arr[n-1]<=s:
            l[n][s]=CountSubset(arr,n-1,s-arr[n-1])+CountSubset(arr,n-1,s)
            return CountSubset(arr,n-1,s-arr[n-1])+CountSubset(arr,n-1,s)
        else:
            l[n][s]=CountSubset(arr,n-1,s)
            return CountSubset(arr,n-1,s)
        
n=6#int(input("Enter No of Element:"))
arr=[2,3,5,6,8,10]#sorted(list(map(int,input().split())))
s=10#int(input("Enter sum to get:"))
l=[[-1]*(s+1) for i in range(n+1)]
ans=CountSubset(arr,n,s)
print(ans)

x=PrettyTable()
x.field_names=[i for i in range(s+1)]
for i in l:
    x.add_row(i)
print(x)