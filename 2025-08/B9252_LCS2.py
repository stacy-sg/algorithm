import sys
input = sys.stdin.readline

str1 =[0] + list(input())
str2 =[0] + list(input())

len1 = len(str1)
len2 = len(str2)

lst = [["" for _ in range(len1)] for _ in range(len2)]

for i in range(1, len2):
    for j in range(1, len1):
        if str1[j] == str2[i]:
            lst[i][j] = lst[i-1][j-1] + str1[j]
        else:
            if len(lst[i][j-1]) > len(lst[i-1][j]):
                lst[i][j] = lst[i][j-1]
            else:
                lst[i][j] = lst[i-1][j]

print(len(lst[-1][-1])-1)
if len(lst[-1][-1]) != 0:
    print(lst[-1][-1])