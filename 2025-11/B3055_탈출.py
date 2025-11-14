from collections import deque

R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]

# 방향: 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water_q = deque()
hog_q = deque()

# 초기 위치 탐색
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            hog_q.append((i, j, 0))  # (x, y, 시간)
        elif board[i][j] == '*':
            water_q.append((i, j))

def spread_water():
    for _ in range(len(water_q)):
        x, y = water_q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == '.':
                    board[nx][ny] = '*'
                    water_q.append((nx, ny))

def move_hog():
    for _ in range(len(hog_q)):
        x, y, t = hog_q.popleft()
        for dir in range(4):
            nx, ny = x + dx[dir], y + dy[dir]
            if 0 <= nx < R and 0 <= ny < C:
                if board[nx][ny] == 'D':
                    return t + 1
                if board[nx][ny] == '.':
                    board[nx][ny] = 'S'
                    hog_q.append((nx, ny, t + 1))
    return None

# BFS 루프
while hog_q:
    spread_water()        # 1. 물 먼저 퍼짐
    res = move_hog()      # 2. 고슴도치 이동
    if res:
        print(res)
        break
else:
    print("KAKTUS")
