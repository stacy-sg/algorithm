from itertools import combinations

def solution(n, q, ans):
    # 1. 쿼리 최적화: 탐색 속도(O(1))를 위해 각 시도(q[i])를 Set으로 변환
    q_sets = [set(query) for query in q]
    m = len(q)
    
    valid_count = 0
    
    # 2. 1부터 n까지의 숫자 중 5개를 고르는 모든 조합 탐색 (최대 142,506개)
    for combo in combinations(range(1, n + 1), 5):
        is_valid = True
        
        # 3. 현재 조합이 모든 시도(query)의 응답(ans)과 정확히 일치하는지 검증
        for i in range(m):
            # 조합(combo)의 숫자 중 q_sets[i]에 포함된 개수 세기
            match_count = sum(1 for num in combo if num in q_sets[i])
            
            # 단 하나라도 응답 결과와 다르면 즉시 가지치기(탈출)
            if match_count != ans[i]:
                is_valid = False
                break
                
        # 4. 모든 시도 조건을 완벽하게 통과한 조합이라면 정답 카운트 증가
        if is_valid:
            valid_count += 1
            
    return valid_count