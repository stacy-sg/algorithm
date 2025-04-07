import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
tmp = 0

for i in range(n):
    tmp = int(input())
    
    if tmp > 0:
        heapq.heappush(heap, -tmp)
    else:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)