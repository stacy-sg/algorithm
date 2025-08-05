def solution(wallet, bill):
    answer = 0
    while True:
        wallet.sort()
        bill.sort()
        
        if wallet[1] <= bill[1] or wallet[0] >= bill[0]:
            break
        
        bill[1] //= 2
        answer += 1
        
    return answer