def solution(nums):
    nums2 = list(set(nums))

    if len(nums)/2 <= len(nums2):
        ans = len(nums)/2
    else:
        ans = len(nums2)
    return ans

solution([3,1,2,3])