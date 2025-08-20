def solution(players, m, k):
    ans = 0
    n = len(players)
    need = [p // m for p in players]
    end = [0] * (n + k + 1)
    
    active = 0
    for t in range(n):
        active -= end[t]
        if active < need[t]:
            add = need[t] - active
            ans += add
            active += add
            if t + k <= n:
                end[t + k] += add
    return ans