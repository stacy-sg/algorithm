import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    n = int(input())
    x, y = 1, 0
    for j in range(n):
        x, y = y, x+y
    print(x, y)