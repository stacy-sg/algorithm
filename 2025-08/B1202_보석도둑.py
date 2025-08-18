import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort(key=lambda x : x[0])
bags.sort()

pq = []
ans = 0
cnt = 0

for c in bags:
    while cnt < N and jewels[cnt][0] <= c:
        heapq.heappush(pq, -jewels[cnt][1])
        cnt += 1
    if pq:
        ans -= heapq.heappop(pq)
    
print(ans)