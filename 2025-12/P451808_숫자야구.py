def solution(n, submit):

    # 1) 가능한 모든 후보 생성 (1~9, 중복 없는 4자리)
    candidates = []
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a: continue
            for c in range(1, 10):
                if c in (a, b): continue
                for d in range(1, 10):
                    if d in (a, b, c): continue
                    candidates.append(int(f"{a}{b}{c}{d}"))

    # STRIKE/BALL 계산 함수
    def get_sb(x, y):
        x = str(x)
        y = str(y)
        S = sum(x[i] == y[i] for i in range(4))
        B = sum(ch in y for ch in x) - S
        return S, B

    # 2) 후보군을 점점 줄여가며 submit 호출
    while len(candidates) > 1:
        cur = candidates[0]
        result = submit(cur)     # "xS yB"
        if result == "4S 0B":
            return cur

        xS, yB = map(int, result.replace("S", "").replace("B", "").split())

        new_list = []
        for c in candidates:
            s, b = get_sb(cur, c)
            if s == xS and b == yB:
                new_list.append(c)

        candidates = new_list

    # 마지막 하나 남으면 정답
    return candidates[0]