import sys
input = sys.stdin.readline

T = int(input())
Qs = [int(input()) for _ in range(T)]
MAX = max(Qs)

f = [0] * (MAX + 1)
for d in range(1, MAX + 1):
    for k in range(d, MAX + 1, d):
        f[k] += d

g = [0] * (MAX + 1)
s = 0
for i in range(1, MAX + 1):
    s += f[i]
    g[i] = s

for n in Qs:
    print(g[n])