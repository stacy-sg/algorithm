def word_to_int(word):
    """문자열을 26진법 숫자로 변환하는 함수"""
    val = 0
    for char in word:
        # 'a'는 1, 'b'는 2, ..., 'z'는 26
        val = val * 26 + (ord(char) - ord('a') + 1)
    return val

def int_to_word(val):
    """숫자를 다시 알파벳 문자열로 역변환하는 함수"""
    res = []
    while val > 0:
        val -= 1  # 1-based 인덱스이므로 1을 빼고 계산해야 'a'부터 딱 맞아떨어짐
        res.append(chr((val % 26) + ord('a')))
        val //= 26
    
    # 일의 자리부터 구했으므로 리스트를 뒤집어서 문자열로 합침
    return "".join(res[::-1])

def solution(n, bans):
    # 1. bans 리스트의 모든 단어를 숫자로 변환
    banned_nums = [word_to_int(word) for word in bans]
    
    # 2. 삭제된 번호들을 오름차순으로 정렬
    banned_nums.sort()
    
    # 3. 목표 숫자 추적 시작
    target = n
    
    # 4. 삭제된 숫자를 보며 target 인덱스 밀어내기
    for b in banned_nums:
        if b <= target:
            target += 1
        else:
            break
            
    # 5. 최종 결정된 숫자를 문자열로 변환하여 반환
    return int_to_word(target)