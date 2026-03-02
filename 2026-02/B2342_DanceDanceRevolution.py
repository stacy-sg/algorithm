import sys

def get_cost(from_pos, to_pos):
    # 이동할 때 드는 힘을 계산하는 함수
    if from_pos == to_pos: 
        return 1
    elif from_pos == 0: 
        return 2
    elif abs(from_pos - to_pos) == 2: 
        return 4
    else: 
        return 3

# 입력이 한 줄에 들어올지 여러 줄에 들어올지 모르므로 전체를 읽어서 리스트로 만듭니다.
steps = list(map(int, sys.stdin.read().split()))

# DP 테이블 초기화: dp[왼발][오른발] = 최소 누적 힘
# 처음에는 아무것도 밟지 않았으므로 무한대(inf)로 설정
INF = float('inf')
dp = [[INF] * 5 for _ in range(5)]
dp[0][0] = 0  # 시작 위치 (0, 0)의 힘은 0

for target in steps:
    if target == 0:  # 입력 종료 조건
        break
        
    # 이번 스텝의 결과를 저장할 새로운 DP 테이블
    next_dp = [[INF] * 5 for _ in range(5)]
    
    # 이전 스텝에서 가능한 모든 발의 위치(i: 왼발, j: 오른발)를 확인
    for i in range(5):
        for j in range(5):
            if dp[i][j] != INF:  # 도달 가능한 상태였다면
                
                # 1. 왼발을 target으로 움직이는 경우 (오른발 j는 그대로)
                # 두 발이 같은 곳에 있으면 안 됨 (단, 시작점 0은 예외)
                if j != target:
                    cost = get_cost(i, target)
                    next_dp[target][j] = min(next_dp[target][j], dp[i][j] + cost)
                    
                # 2. 오른발을 target으로 움직이는 경우 (왼발 i는 그대로)
                if i != target:
                    cost = get_cost(j, target)
                    next_dp[i][target] = min(next_dp[i][target], dp[i][j] + cost)
                    
    # 다음 스텝을 위해 DP 테이블 갱신
    dp = next_dp
    
# 모든 지시를 마친 후, 가능한 상태 중 가장 힘이 적게 든 값을 찾음
min_power = INF
for i in range(5):
    for j in range(5):
        min_power = min(min_power, dp[i][j])
        
print(min_power)