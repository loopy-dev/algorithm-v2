"""
A pangram is a string that contains every letter of the alphabet. 
Given a sentence determine whether it is a pangram in the English alphabet. 
Ignore case. Return either pangram or not pangram as appropriate.
모든 알파벳이 들어있으면 그것은 pangram이다.
그렇지 않다면, not pangram이다.
"""
"""
1. 문자열을 순회하면서 해당 문자열을 다른 곳에 추가한다.
2. 공백은 카운트하지 않는다.
3. 추가한 곳의 길이가 26개이면 모든 알파벳이 존재하므로, pangram이라고 할 수 있다.
3-1. 대문자라면, 소문자로 바꾼 다음에 처리해야 한다.
"""



def is_pangrams(s):
    # 자료를 보관하기 위한 자료구조
    alphabets = set()


    for c in s:
        current = c

        # c가 띄어쓰기라면 어무 처리도 하지 않는다.
        if current == ' ':
            continue
        
        # 대문자는 소문자로 바꾼 다음 저장한다.
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            current = chr(ord(c) + 32)
        
        alphabets.add(current)
    
    if len(alphabets) == 26:
        return True
    
    return False


def pangrams(s):
    return 'pangram' if is_pangrams(s) else 'not pangram'

