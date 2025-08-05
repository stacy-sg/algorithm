import sys
input = sys.stdin.readline

N = int(input())

dw =[list(map(int, input().split())) for _ in range(N)]

dw.sort()

possible = []
ans = 0

for i in range(n, 0, -1):
    while dw and dw[-1][0] >= i:
        possible.append(dw.pop()[1])

    if possible:
        possible.sort()
        ans += possible.pop()

print(ans)