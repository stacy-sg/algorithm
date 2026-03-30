import heapq
from collections import defaultdict

def solution(city, road):
    # 1. 소수점 방지를 위해 모든 좌표를 2배로 스케일링
    scaled_city = [(x * 2, y * 2) for x, y in city]
    scaled_road = [(x1 * 2, y1 * 2, x2 * 2, y2 * 2, v) for x1, y1, x2, y2, v in road]
    
    pois = set(scaled_city) # 관심 지점(Nodes) 수집용 Set
    h_roads = [] # 가로 도로
    v_roads = [] # 세로 도로
    
    # 2. 도로 분류 및 카메라 위치, 끝점 수집
    for x1, y1, x2, y2, v in scaled_road:
        pois.add((x1, y1))
        pois.add((x2, y2))
        
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2 # 정중앙 카메라 위치
        pois.add((mx, my))
        
        if y1 == y2: # Y좌표가 같으면 가로 도로
            h_roads.append((min(x1, x2), max(x1, x2), y1, v))
        else:        # X좌표가 같으면 세로 도로
            v_roads.append((x1, min(y1, y2), max(y1, y2), v))
            
    # 교차점 수집 (가로 도로와 세로 도로가 만나는 지점)
    for hx1, hx2, hy, hv in h_roads:
        for vx, vy1, vy2, vv in v_roads:
            if hx1 <= vx <= hx2 and vy1 <= hy <= vy2:
                pois.add((vx, hy))
                
    # 3. 각 노드의 제한 속도 기록 (기본값 무한대)
    INF = float('inf')
    limit = {p: INF for p in pois}
    
    # 카메라가 있는 위치만 제한 속도 갱신 (더 빡빡한 속도로)
    for x1, y1, x2, y2, v in scaled_road:
        mx, my = (x1 + x2) // 2, (y1 + y2) // 2
        limit[(mx, my)] = min(limit[(mx, my)], v)
        
    # 4. 간선(Edge) 연결하기
    points_by_y = defaultdict(list)
    points_by_x = defaultdict(list)
    for x, y in pois:
        points_by_y[y].append((x, y))
        points_by_x[x].append((x, y))
        
    adj = defaultdict(list)
    
    # 가로 선상의 인접한 점들이 도로에 포함되는지 확인 후 연결
    h_segs_by_y = defaultdict(list)
    for hx1, hx2, hy, v in h_roads:
        h_segs_by_y[hy].append((hx1, hx2))
        
    for y, points in points_by_y.items():
        points.sort()
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i+1]
            for sx1, sx2 in h_segs_by_y[y]:
                if sx1 <= p1[0] and p2[0] <= sx2: # 도로 구간 안에 있다면
                    adj[p1].append(p2)
                    adj[p2].append(p1)
                    break
                    
    # 세로 선상의 인접한 점들이 도로에 포함되는지 확인 후 연결
    v_segs_by_x = defaultdict(list)
    for vx, vy1, vy2, v in v_roads:
        v_segs_by_x[vx].append((vy1, vy2))
        
    for x, points in points_by_x.items():
        points.sort()
        for i in range(len(points) - 1):
            p1, p2 = points[i], points[i+1]
            for sy1, sy2 in v_segs_by_x[x]:
                if sy1 <= p1[1] and p2[1] <= sy2:
                    adj[p1].append(p2)
                    adj[p2].append(p1)
                    break
                    
    # 5. 다익스트라 (Max-Min Path)
    start_node = scaled_city[0]
    max_speed = {p: -1 for p in pois}
    
    # 시작점의 제한 속도 파악 후 힙에 삽입 (파이썬은 Min-Heap이므로 음수로 변환)
    start_limit = limit[start_node]
    max_speed[start_node] = start_limit
    pq = [(-start_limit, start_node)]
    
    while pq:
        curr_speed, u = heapq.heappop(pq)
        curr_speed = -curr_speed # 원래의 양수 속도로 복원
        
        # 이미 더 나은 경로를 찾은 상태라면 스킵
        if curr_speed < max_speed[u]:
            continue
            
        for v in adj[u]:
            # 다음 지점으로 이동할 때, 현재 유지 중인 속도와 다음 지점의 카메라 단속 속도 중 작은 값으로 병목 발생
            next_speed = min(curr_speed, limit[v])
            
            # 새롭게 구한 속도가 기존에 알려진 속도보다 더 높다면 갱신
            if next_speed > max_speed[v]:
                max_speed[v] = next_speed
                heapq.heappush(pq, (-next_speed, v))
                
    # 6. 최종 결과 정리
    answer = []
    # 2번 도시부터 n번 도시까지 순회 (인덱스 1부터 시작)
    for i in range(1, len(scaled_city)):
        target = scaled_city[i]
        res = max_speed[target]
        if res == INF:
            answer.append(0) # 카메라를 한 번도 안 거침
        else:
            answer.append(res)
            
    return answer