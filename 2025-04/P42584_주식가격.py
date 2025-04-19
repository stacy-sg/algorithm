from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    
    while q:
        price = q.popleft()
        cnt = 0
        
        for i in q:
            cnt += 1
            if price > i:
                break
        answer.append(cnt)
        
    return answer