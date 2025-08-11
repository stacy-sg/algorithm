import sys
input = sys.stdin.readline

str1 = [""] + list(input())
str2 = [""] + list(input())

lst = [[""]* len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            lst[i][j] = lst[i-1][j-1] + str1[i]
        else:
            if len(lst[i-1][j]) >= len(lst[i][j-1]):
                lst[i][j] = lst[i-1][j]
            else:
                lst[i][j] = lst[i][j-1]

print(len(lst[-1][-1]))
print(lst[-1][-1])