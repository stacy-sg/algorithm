import sys

input = sys.stdin.readline


n = int(input().strip())
used_keys = set()

for _ in range(n):
    option = input().rstrip("\n") # 공백을 보존하기 위해 rstrip("\n")만 사용
    
    # 1. 단어의 첫 글자 인덱스들 찾기
    # 항상 0번 인덱스는 첫 글자이고, 공백 바로 다음 인덱스도 첫 글자입니다.
    first_letter_indices = [0]
    for i in range(len(option) - 1):
        if option[i] == ' ':
            first_letter_indices.append(i + 1)
            
    assigned = False
    
    # 2. 규칙 1: 단어의 첫 글자부터 확인
    for idx in first_letter_indices:
        char = option[idx].lower() # 대소문자 구분을 없애기 위해 소문자로 변환하여 확인
        
        if char not in used_keys:
            used_keys.add(char)
            # 원본을 훼손하지 않고 괄호를 씌워 새로운 문자열 생성
            res = option[:idx] + "[" + option[idx] + "]" + option[idx+1:]
            print(res)
            assigned = True
            break
            
    if assigned:
        continue
        
    # 3. 규칙 2: 모든 글자 왼쪽부터 확인 (규칙 1에서 지정 못한 경우)
    for idx in range(len(option)):
        char = option[idx]
        
        # 공백은 단축키가 될 수 없으므로 무시
        if char != ' ' and char.lower() not in used_keys:
            used_keys.add(char.lower())
            res = option[:idx] + "[" + option[idx] + "]" + option[idx+1:]
            print(res)
            assigned = True
            break
            
    # 4. 규칙 3: 어떠한 것도 지정할 수 없는 경우 원본 그대로 출력
    if not assigned:
        print(option)