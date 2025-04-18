from itertools import permutations

def solution(numbers):
    s = []
    p = []
    answer = 0
    for i in range(1, len(numbers)+1):
        s.append(list(set(map(''.join, permutations(numbers, i)))))
    sp = list(set(map(int, set(sum(s, [])))))
    for n in sp:
        if n < 2:
            p.append(0)
        else:
            flag = 0
            for i in range(2, n):
                if n % i == 0:
                    p.append(0)
                    flag = 1
                    break
            if flag == 0:
                p.append(1)
                answer = sum(p) 
    return answer