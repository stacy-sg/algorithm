import sys
input = sys.stdin.readline

n = int(input())

nums = [1, 1, 1]

for i in range(3, 100):
    nums.append(nums[i-2]+nums[i-3])

for i in range(n):
    p = int(input().strip())
    print(nums[p-1])