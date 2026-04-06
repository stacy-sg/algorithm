import sys
import math

input_data = sys.stdin.read().split()

# 입력이 비어있을 경우 스크립트 즉시 종료
if not input_data:
    sys.exit(0)

n = int(input_data[0])

# 2. 전역 상태 변수 초기화
b_prev = 0
G = 0
max_b = 0
valid = True

# 3. 로그 데이터 순회 (인덱스 1부터 시작하여 2개씩 추출)
idx = 1
for _ in range(n):
    a = int(input_data[idx])
    b = int(input_data[idx+1])
    idx += 2
    
    # [분기 1] 충전이 필요 없는 경우 (입금, 또는 기존 잔액으로 커버 가능한 출금)
    if a > 0 or b_prev + a >= 0:
        if b_prev + a != b:
            valid = False
            break
            
    # [분기 2] 잔액 부족으로 시스템 내부 충전이 발생한 경우
    else:
        d = b - b_prev - a  # 내부적으로 충전된 금액 역산
        
        # 충전액이 0 이하로 계산되면 명백한 논리적 모순
        if d <= 0:
            valid = False
            break
            
        G = math.gcd(G, d)     # 모든 충전액들의 최대공약수 누적 갱신
        max_b = max(max_b, b)  # 충전 이벤트 발생 시점의 최대 잔액 갱신
        
    b_prev = b

# 4. 상태 변수에 따른 최종 결과 판별 및 출력
if not valid:
    print("-1")
elif G == 0:
    # 모순은 없으나 충전이 단 한 번도 발생하지 않은 경우
    print("1")
elif G > max_b:
    # 도출된 최대공약수가 '충전 후 남은 최대 잔액'보다 커야만 유효함
    print(G)
else:
    print("-1")