def solution(cost, hint):
    n = len(cost)
    min_cost = float('inf')

    # 마지막 스테이지를 제외한 n-1개에서 번들 구매 여부를 비트마스크로 표현
    for mask in range(1 << (n - 1)):
        bundle_cost = 0
        hints = [0] * (n + 1)  # hints[i]: i번 스테이지에서 사용 가능한 힌트권 수 (1-indexed)

        # 비트가 1인 스테이지에서 번들 구매
        for i in range(n - 1):
            if mask & (1 << i):
                bundle_cost += hint[i][0]  # 번들 구매 비용

                # 번들에 포함된 힌트권을 해당 스테이지 카운트에 추가
                for j in range(1, len(hint[i])):
                    stage_num = hint[i][j]
                    hints[stage_num] += 1

        # 각 스테이지 클리어 비용 합산
        stage_cost = 0
        for i in range(1, n + 1):
            # 사용 가능한 힌트권은 최대 n-1개로 제한
            used = min(hints[i], n - 1)
            stage_cost += cost[i - 1][used]

        min_cost = min(min_cost, bundle_cost + stage_cost)

    return min_cost