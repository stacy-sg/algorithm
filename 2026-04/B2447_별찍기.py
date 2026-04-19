import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N = int(input())

# N×N 격자
grid = [[' '] * N for _ in range(N)]

def fill(n, r, c):
    if n == 3:
        # 3×3 기저 사례: 가운데(r+1, c+1)만 공백, 나머지는 별
        for dr in range(3):
            for dc in range(3):
                if not (dr == 1 and dc == 1):
                    grid[r + dr][c + dc] = '*'
        return

    third = n // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:   # 가운데 블록: 공백 유지
                continue
            fill(third, r + i * third, c + j * third)  # 나머지 8블록 재귀

fill(N, 0, 0)

print('\n'.join(''.join(row).rstrip() for row in grid))