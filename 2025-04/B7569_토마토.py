from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())

lst = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

q = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

ans = 0

def bfs():
    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue

            if lst[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:
                q.append((nx,ny,nz))
                lst[nx][ny][nz] = lst[x][y][z] + 1
                visited[nx][ny][nz] = True

for i in range(h):
    for j in range(n):
        for k in range(m):
            if lst[i][j][k] == 1 and visited[i][j][k] == 0:
                q.append((i,j,k))
                visited[i][j][k] = True

bfs()

for i in lst:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(j))

print(ans-1)