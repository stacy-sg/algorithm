def total_time(L, diffs, times, limit):
    total = 0
    n = len(diffs)
    for i in range(n):
        if diffs[i] <= L:
            total += times[i]
        else:
            fails = diffs[i] - L
            if i == 0:
                total += fails * times[i] + times[i]
            else:
                total += fails * (times[i] + times[i-1]) + times[i]
        if total > limit:
            return total
    return total

def solution(diffs, times, limit):
    minimum, maximum = 1, max(diffs)
    ans = maximum
    while minimum <= maximum:
        mid = (minimum + maximum) // 2
        if total_time(mid, diffs, times, limit) <= limit:
            ans = mid
            maximum = mid - 1
        else:
            minimum = mid + 1
    return ans