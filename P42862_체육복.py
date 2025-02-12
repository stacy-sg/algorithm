def solution(n, lost, reserve):
    answer = 0

    lost = [l for l in lost if l not in reserve]
    reserve = [r for r in reserve if r not in lost]
    
    lost_tmp = sorted(lost).copy()
    
    for l in lost_tmp:
        if (l-1) in reserve:
            lost.remove(l)
            reserve.remove(l-1)
            
        elif (l+1) in reserve:
            lost.remove(l)
            reserve.remove(l+1)

    answer = n - len(lost)
    
    return answer