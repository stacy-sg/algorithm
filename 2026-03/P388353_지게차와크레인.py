from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    # 1. 패딩을 추가한 창고 배열 생성 (가장자리를 빈 공간 '.' 으로 감쌈)
    grid = [['.'] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            grid[i + 1][j + 1] = storage[i][j]
            
    # 상하좌우 이동을 위한 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 2. 요청 순회
    for req in requests:
        target = req[0]
        
        # 3. 크레인 (길이 2): 창고 내부의 타겟 컨테이너를 모두 조건 없이 제거
        if len(req) == 2:
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    if grid[i][j] == target:
                        grid[i][j] = '.'
        
        # 4. 지게차 (길이 1): 외부 공기와 닿아있는 타겟 컨테이너만 제거
        else:
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            q = deque([(0, 0)])  # 항상 패딩된 가장자리인 (0, 0)부터 공기 탐색 시작
            visited[0][0] = True
            
            to_remove = set()  # 한 번에 지우기 위해 제거 후보 좌표를 담을 셋
            
            while q:
                x, y = q.popleft()
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    
                    if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                        # 빈 공간이면 공기가 통하므로 큐에 넣고 계속 탐색
                        if grid[nx][ny] == '.':
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            
                        # 타겟 컨테이너가 공기와 맞닿아 있다면 제거 후보로 등록
                        elif grid[nx][ny] == target:
                            visited[nx][ny] = True
                            to_remove.add((nx, ny))
            
            # 탐색이 끝난 후 후보군 컨테이너들을 일괄 제거
            for rx, ry in to_remove:
                grid[rx][ry] = '.'
                
    # 5. 모든 요청을 마친 후 남아있는 컨테이너 수 계산
    answer = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] != '.':
                answer += 1
                
    return answer