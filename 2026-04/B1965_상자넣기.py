import sys

input = sys.stdin.readline

n = int(input().strip())
boxes = list(map(int, input().split()))

# dp[i]: i번째 상자를 마지막으로 선택했을 때의 최대 상자 개수
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        # j 상자가 i 상자보다 작으면 j → i 방향으로 넣기 가능
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 모든 끝점 중 가장 긴 값이 정답
print(max(dp))