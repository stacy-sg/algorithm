import sys
input = sys.stdin.readline

n = int(input())

lst = [0] * 10001

for i in range(n):
    lst[int(input())] += 1

for i in range(10001):
    if lst[i] !=0:
        for j in range(lst[i]):
            print(i)