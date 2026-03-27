import sys

input = sys.stdin.readline

# 입력 받기
n, c = map(int, input().split())
weights = list(map(int, input().split()))

# 1. 투 포인터를 사용하기 위해 오름차순 정렬
weights.sort()

# 정답을 찾았는지 여부를 기록할 플래그 변수
found = False

# [시나리오 1] 1개의 물건으로 C를 만들 수 있는지 확인
if c in set(weights):
    found = True

# [시나리오 2] 2개의 물건으로 C를 만들 수 있는지 탐색
# 시나리오 1에서 못 찾았을 때만 실행
if not found:
    left, right = 0, n - 1
    while left < right:
        current_sum = weights[left] + weights[right]
        
        if current_sum == c:
            found = True
            break  # 정답을 찾으면 즉시 while문 탈출
        elif current_sum < c:
            left += 1
        else:
            right -= 1

# [시나리오 3] 3개의 물건으로 C를 만들 수 있는지 탐색
# 시나리오 1, 2에서 못 찾았을 때만 실행
if not found:
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        target = c - weights[i]
        
        while left < right:
            current_sum = weights[left] + weights[right]
            
            if current_sum == target:
                found = True
                break  # 안쪽 while문 탈출
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        # 정답을 찾았다면 바깥쪽 for문도 탈출
        if found:
            break

# 최종 결과 출력
if found:
    print(1)
else:
    print(0)