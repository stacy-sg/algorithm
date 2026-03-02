import sys

input = sys.stdin.readline

n = int(input().strip())

prefixes = set()           # 모든 접두사를 저장할 해시셋 (O(1) 검색 속도)
nickname_count = dict()    # 똑같은 닉네임의 등장 횟수를 셀 딕셔너리

for _ in range(n):
    name = input().strip()
    
    # 1. 닉네임 등장 횟수 카운트
    nickname_count[name] = nickname_count.get(name, 0) + 1
    
    alias = ""
    found = False
    
    # 2. 접두사를 한 글자씩 늘려가며 확인
    for i in range(1, len(name) + 1):
        prefix = name[:i]
        
        # 3. 아직 사용되지 않은 가장 짧은 접두사 발견!
        if not found and prefix not in prefixes:
            alias = prefix
            found = True # 별칭은 찾았지만, 나중을 위해 반복문을 멈추지 않습니다.
            
        # 4. 나중에 들어올 유저를 위해 현재 닉네임의 모든 접두사를 Set에 저장
        prefixes.add(prefix)
    
    # 5. 모든 접두사가 이미 존재해서 별칭을 찾지 못한 경우
    if not found:
        count = nickname_count[name]
        if count == 1:
            alias = name
        else:
            alias = name + str(count)
            
    print(alias)