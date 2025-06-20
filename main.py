import math
arr=list(map(int,input().split()))
k=int(input())
start=0
c=0
m=0
for end in range(0,len(arr)):
    if arr[end]%2!=0:
        c+=1
        if end-start+1==k:
           
            m=max(m,c)
            start+=1
print(m)            
            
    
            
        




