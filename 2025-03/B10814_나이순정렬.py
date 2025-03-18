import sys
input = sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    lst.append((age, name))

lst.sort(key= lambda x : x[0])

for i in lst:
    print(i[0], i[1])