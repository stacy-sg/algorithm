import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
answer = [0]
tmp = 0

for i in lst:
    tmp += i
    answer.append(tmp)

for i in range(m):
    x, y = map(int, input().split())
    print(answer[y]-answer[x-1])