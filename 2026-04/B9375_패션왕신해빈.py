import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    category = defaultdict(int)  # 의상 종류별 개수 저장

    for _ in range(n):
        name, kind = input().split()
        category[kind] += 1  # 종류별 카운트

    ans = 1
    for cnt in category.values():
        ans *= (cnt + 1)  # 해당 종류에서 안 입는 경우 1가지 포함

    ans -= 1  # 전부 안 입는 경우(알몸) 제거
    print(ans)