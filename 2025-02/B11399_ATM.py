n=int(input())
arr=list(map(int,input().split()))
arr.sort()
result=0
time=0
for i in range(n):
    time+=arr[i]
    result+=time
print(result)