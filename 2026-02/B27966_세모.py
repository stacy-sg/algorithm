import sys

input = sys.stdin.readline

# 1. 정점의 개수 입력
n = int(input().strip())

# 2. 모든 정점 쌍의 거리 합 최솟값 출력
print((n - 1) ** 2)

# 3. 트리를 이루는 간선 정보 출력 
# (1번 정점을 중심으로 2번부터 N번까지 모두 연결)
for i in range(2, n + 1):
    print(f"1 {i}")