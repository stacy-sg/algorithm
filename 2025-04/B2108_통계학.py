from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

print(round(sum(nums) / len(nums))) #평균값
print(nums[len(nums)//2]) #중앙값

#최빈값
cnt = Counter(nums)

if len(cnt) != 1:
  mode = cnt.most_common(2)
  if mode[0][1] == mode[1][1]:
    print(mode[1][0])
  else:
    print(mode[0][0])
else:
  mode = cnt.most_common(1)
  print(mode[0][0])

print(max(nums)-min(nums)) #범위