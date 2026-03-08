import sys
from collections import deque

# 코딩테스트 입력 속도 최적화
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    a, b = map(int, input().split())
    
    # 중복 탐색 방지를 위한 방문 배열 (0 ~ 9999)
    visited = [False] * 10000
    visited[a] = True
    
    # 큐에는 (현재 숫자, 지금까지의 명령어 경로)를 함께 저장
    q = deque([(a, "")])
    
    while q:
        n, path = q.popleft()
        
        # 목표 숫자에 도달하면 명령어 경로 출력 후 현재 테스트 케이스 종료
        if n == b:
            print(path)
            break
        
        # 1. D 연산
        num_d = (n * 2) % 10000
        if not visited[num_d]:
            visited[num_d] = True
            q.append((num_d, path + "D"))
            
        # 2. S 연산: 파이썬은 (-1) % 10000 = 9999 가 됨
        num_s = (n - 1) % 10000
        if not visited[num_s]:
            visited[num_s] = True
            q.append((num_s, path + "S"))
            
        # 3. L 연산: 1234 -> 2341
        # (1234 % 1000) * 10 -> 2340
        # 1234 // 1000 -> 1
        # 2340 + 1 -> 2341
        num_l = (n % 1000) * 10 + (n // 1000)
        if not visited[num_l]:
            visited[num_l] = True
            q.append((num_l, path + "L"))
            
        # 4. R 연산: 1234 -> 4123
        # (1234 % 10) * 1000 -> 4000
        # 1234 // 10 -> 123
        # 4000 + 123 -> 4123
        num_r = (n % 10) * 1000 + (n // 10)
        if not visited[num_r]:
            visited[num_r] = True
            q.append((num_r, path + "R"))