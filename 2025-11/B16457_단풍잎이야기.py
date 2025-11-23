from itertools import combinations
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

quests = []
for _ in range(m):
    skill_list = list(map(int, input().split()))
    mask = 0
    for x in skill_list:
        mask |= (1 << (x - 1))
    quests.append(mask)

skills = list(range(1, 2 * n + 1))

best = 0

for comb in combinations(skills, n):
    chosen = 0
    for s in comb:
        chosen |= (1 << (s - 1))

    cnt = 0
    for q_mask in quests:
        if (q_mask & chosen) == q_mask:
            cnt += 1

    best = max(best, cnt)

print(best)