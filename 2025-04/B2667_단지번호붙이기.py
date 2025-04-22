from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def bfs(graph, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q= deque()

    cnt = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:

ans = [bfs(graph, i, j) for i in range(n) for j in range(n) if graph[i][j] == 1]

ans.sort()
print(len(ans))

for i in range(len(ans)):
    print(ans[i])