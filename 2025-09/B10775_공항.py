import sys
input = sys.stdin.readline

G = int(input())
P = int(input())
parent = list(range(G+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

ans = 0
for _ in range(P):
    g = int(input())
    x = find(g)
    if x == 0:
        break
    ans += 1
    parent[x] = find(x-1)

print(ans)