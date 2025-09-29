from itertools import combinations
from collections import Counter

def solution(dice):
    n = len(dice)
    k = n // 2

    def sum_frequencies(dice_list):
        # 주어진 주사위들의 가능한 합과 빈도를 Counter로 반환
        freq = Counter()
        freq[0] = 1
        for die in dice_list:
            new = Counter()
            for s, c in freq.items():
                for face in die:
                    new[s + face] += c
            freq = new
        return freq

    best_win = -1
    best_pick = None

    for comb in combinations(range(n), k):
        A_idx = set(comb)
        B_idx = [i for i in range(n) if i not in A_idx]

        freqA = sum_frequencies([dice[i] for i in A_idx])
        freqB = sum_frequencies([dice[i] for i in B_idx])

        minB = min(freqB.keys())
        maxB = max(freqB.keys())

        # prefixB[t] = B 합이 t 이하인 경우의 수
        prefixB = [0] * (maxB + 1)
        for s, c in freqB.items():
            prefixB[s] += c
        for i in range(1, maxB + 1):
            prefixB[i] += prefixB[i - 1]

        win_cases = 0
        for sA, cntA in freqA.items():
            # B 합이 sA보다 작은 경우의 수
            if sA <= 0:
                less = 0
            elif sA - 1 >= maxB:
                less = prefixB[maxB]
            else:
                less = prefixB[sA - 1]
            win_cases += cntA * less

        if win_cases > best_win:
            best_win = win_cases
            best_pick = sorted([i + 1 for i in A_idx])  # 1-based

    return best_pick