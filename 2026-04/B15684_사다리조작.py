import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

# ladder[h][b] = 1: 높이 h에서 b번~b+1번 세로선 연결
# 인덱스 범위를 넉넉히 잡아 경계 조건 예외 방지
ladder = [[0] * (N + 2) for _ in range(H + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[a][b] = 1

def check():
    # 모든 세로선 i가 i번에 도착하면 True
    for start in range(1, N + 1):
        col = start
        for h in range(1, H + 1):
            if ladder[h][col] == 1:        # 오른쪽 가로선 존재
                col += 1
            elif ladder[h][col - 1] == 1:  # 왼쪽 가로선 존재
                col -= 1
        if col != start:
            return False
    return True

ans = -1

def dfs(cnt, limit, pos):
    global ans
    # 목표 개수만큼 추가했으면 검증
    if cnt == limit:
        if check():
            ans = limit
            return True
        return False

    # pos 이후 위치만 탐색하여 같은 조합 중복 방지
    for i in range(pos, H * (N - 1)):
        h = i // (N - 1) + 1  # 높이 (1~H)
        b = i % (N - 1) + 1   # 세로선 번호 (1~N-1)

        # 현재 위치와 양쪽 인접 위치에 가로선이 없어야 배치 가능
        if ladder[h][b] == 0 and ladder[h][b - 1] == 0 and ladder[h][b + 1] == 0:
            ladder[h][b] = 1                        # 가로선 추가
            if dfs(cnt + 1, limit, i + 1):          # 다음 위치부터 탐색
                return True
            ladder[h][b] = 0                        # 백트래킹: 원상복구

    return False

# 추가 가로선 수를 0~3으로 제한
for limit in range(4):
    if dfs(0, limit, 0):
        break

print(ans)