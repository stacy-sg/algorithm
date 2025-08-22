import sys
input = sys.stdin.readline

V, E = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(E) ]

parent = list(range(V+1))
rank = [0]*(V+1)

def find(x):
    while parent[x] != x:
        parent [x] = parent[parent[x]]
        x = parent[parent[x]]
    return x

def union(a, b):
    a, b = find(a), find(b)
    if a==b: return False
    if rank[a] < rank[b]:
        parent[a] = b
    elif rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[b] = a
        rank[a] += 1
    return True

edges.sort(key=lambda x: x[2])
ans = 0
cnt = 0
for a, b, w in edges:
    if union(a, b):
        ans += w
        cnt += 1
        if cnt == V-1:
            break

print(ans)