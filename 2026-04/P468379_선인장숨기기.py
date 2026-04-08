def solution(m, n, h, w, drops):
    def check(t):
        # 1. 2차원 누적 합을 위한 배열 초기화 (1-indexed 사용)
        P = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 2. t번째 빗방울까지 격자에 표시
        for k in range(t):
            r, c = drops[k]
            P[r + 1][c + 1] = 1
            
        # 3. 2차원 누적 합 계산
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] += P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1]
                
        # 4. h x w 영역을 순회하며 빗방울이 0개인 안전 구역 탐색
        # (행 -> 열 순으로 순회하므로 가장 위, 왼쪽 좌표가 최초로 발견됨)
        for i in range(h, m + 1):
            for j in range(w, n + 1):
                # O(1) 시간으로 h x w 영역 내의 빗방울 개수 산출
                rain_count = P[i][j] - P[i - h][j] - P[i][j - w] + P[i - h][j - w]
                
                if rain_count == 0:
                    return True, [i - h, j - w] # 0-indexed로 변환하여 반환
                    
        return False, []

    # 이분 탐색 초기 세팅
    left = 0
    right = len(drops)
    best_coord = [0, 0]
    
    while left <= right:
        mid = (left + right) // 2
        possible, coord = check(mid)
        
        if possible:
            # 안전 구역을 찾았다면 해당 좌표를 저장하고, 더 오래 버틸 수 있는지 탐색
            best_coord = coord
            left = mid + 1
        else:
            # 안전 구역이 없다면 시간을 줄여야 함
            right = mid - 1
            
    return best_coord