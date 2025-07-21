import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    n, s = map(int, input().split())
    d = sorted(list(map(int, input().split())))
    start = 1
    end = max(d)
    while start <= end:
        mid = (start+end)//2
        left=d[0]
        cnt = 1
        for i in range(1, n):
            right=d[i]
            if abs(right-left)>=mid:
                cnt += 1
                left=d[i]
        if cnt>=s:
            start=mid+1
        else:
            end=mid-1
    print(end)