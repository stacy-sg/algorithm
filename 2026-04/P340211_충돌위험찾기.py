def solution(points, routes):
    def get_path(route):
        path = []
        coords = [points[p - 1] for p in route]  # 포인트 번호 → 좌표 변환 (1-indexed)

        r, c = coords[0]
        path.append((r, c))  # 출발 좌표 포함

        for i in range(1, len(coords)):
            nr, nc = coords[i]

            # r 좌표 먼저 이동
            while r != nr:
                r += 1 if nr > r else -1
                path.append((r, c))

            # c 좌표 이동
            while c != nc:
                c += 1 if nc > c else -1
                path.append((r, c))

        return path

    # 모든 로봇의 시간별 경로 사전 계산
    robot_paths = [get_path(route) for route in routes]

    max_time = max(len(p) for p in robot_paths)

    danger = 0

    for t in range(max_time):
        pos_count = {}

        for path in robot_paths:
            if t >= len(path):      # 이미 운송 완료한 로봇은 제외
                continue
            pos = path[t]
            pos_count[pos] = pos_count.get(pos, 0) + 1

        # 2대 이상이 모인 좌표 수만큼 위험 상황 카운트
        for cnt in pos_count.values():
            if cnt >= 2:
                danger += 1

    return danger