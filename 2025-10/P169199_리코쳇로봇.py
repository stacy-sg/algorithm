from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                start = (i, j)
            elif board[i][j] == "G":
                goal = (i, j)
    
    q = deque()
    q.append((start[0], start[1], 0))  # (x, y, 이동 횟수)
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while q:
        x, y, cnt = q.popleft()

        if (x, y) == goal:
            return cnt

        for dx, dy in dirs:
            nx, ny = x, y
            while 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                nx += dx
                ny += dy

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, cnt + 1))

    return -1