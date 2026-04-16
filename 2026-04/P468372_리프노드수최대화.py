def solution(dist_limit, split_limit):
    ans = 1  # 분배 노드 0개: 루트의 자식 1개가 곧 리프

    p2 = 1      # 2^n: n번의 2-레벨 이후 프론티어 크기
    dist_n = 0  # n번의 2-레벨에 사용한 분배 노드 총합

    for n in range(31):       # 2^31 > 10^9이므로 n은 최대 30
        if p2 > split_limit:  # 분배도 초과 → 이 이상은 불필요
            break
        if dist_n > dist_limit:  # 예산 초과 → 이 이상도 불필요
            break

        p3 = 1      # 3^m: m번의 3-레벨 이후 추가 배율
        dist_m = 0  # m번의 3-레벨에 사용한 분배 노드 총합

        for m in range(20):      # 3^20 > 10^9이므로 m은 최대 19
            p = p2 * p3          # 현재 프론티어 크기 = 리프의 분배도
            if p > split_limit:
                break

            dist_used = dist_n + dist_m
            if dist_used > dist_limit:  # 이미 예산 초과 → m 더 늘려도 소용없음
                break

            remaining = dist_limit - dist_used
            x = min(p, remaining)  # 부분 확장 가능한 노드 수

            # 부분 레벨 추가: c=3이 가능하면 c=3, 아니면 c=2, 불가면 현상 유지
            if p * 3 <= split_limit:
                ans = max(ans, p + 2 * x)  # x노드를 3자녀로 확장 시 +2x 리프
            elif p * 2 <= split_limit:
                ans = max(ans, p + x)      # x노드를 2자녀로 확장 시 +x 리프
            else:
                ans = max(ans, p)          # 분배도 한계로 더 확장 불가

            # 다음 m 준비: 현재 p 크기의 프론티어를 분배 노드로 소모
            dist_m += p2 * p3
            p3 *= 3

        # 다음 n 준비: 현재 p2 크기의 프론티어를 분배 노드로 소모
        dist_n += p2
        p2 *= 2

    return ans