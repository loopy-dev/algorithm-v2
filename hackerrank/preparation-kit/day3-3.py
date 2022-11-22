"""
caesar cipher
alphabet encrypt
암호화 방식은 알파벳 + 3 (ord)하여 암호화를 진행하는 것이다.
주의: 오직 알파벳만 암호화한다.
"""


def caesarCipher(s, k):
    """
    s와 k(rotation 횟수)가 주어졌을 때, encrypted string 구하기
    (ord(s) - ord('a')) % ord('a') + ord('a')
    abcde
    fghij
    klmno
    pqrst
    uvwxy
    z
    """
    # Write your code here
    string = ""
    for c in s:
        # c가 알파벳이고 lowercase 범위에 있다면
        if ord("a") <= ord(c) <= ord("z"):
            new_char = chr((ord(c) - ord("a") + k) % 26 + ord("a"))
            string += new_char

        # c가 알파벳이고 UPPERCASE 범위에 있다면
        elif ord("A") <= ord(c) <= ord("Z"):
            new_char = chr((ord(c) - ord("A") + k) % 26 + ord("A"))
            string += new_char

        # 나머지
        else:
            string += c

    return string
