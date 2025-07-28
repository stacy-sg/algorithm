import sys
sys.setrecursionlimit(10 ** 6)
from collections import defaultdict

def solution(info, n, m):
    totalNum = len(info)
    candidates = []
    info.sort(key=lambda x: (-x[1], -x[0]))
    visited = defaultdict(int)
    
    def steal(evidA, evidB, idx):
        if len(candidates) and evidA >= min(candidates):
            return
        if evidA >= n or evidB >= m:
            return
        if idx == totalNum:
            candidates.append(evidA)
            return
        
        visited[(evidA, evidB, idx)] += 1

        newB = evidB + info[idx][1]
        if not visited[(evidA, newB, idx+1)] and newB < m:
            steal(evidA, newB, idx+1)
        newA = evidA + info[idx][0]
        if not visited[(newA, evidB, idx+1)] and newA < n:
            steal(evidA + info[idx][0], evidB, idx+1)

    steal(0, 0, 0)
    
    return -1 if len(candidates) == 0 else min(candidates)