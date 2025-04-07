import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    visited[start] = 1
    q = deque([start])

    while q:
        friend = q.popleft()

        for i in graph[friend]:
            if not visited[i]:
                visited[i] = visited[friend] + 1
                q.append(i)

n, m = map(int, input().split())
graph =[[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    bfs(i)
    ans.append(sum(visited))

print(ans.index(min(ans))+1)