"""
Caesar Cipher

알파벳에 숫자를 더하여 새로운 문자열을 반환한다.
이때, 알파벳이 아닌 문자열은 변환하지 않는다.
"""
"""
1. 주어지는 문자열이 대문자인지 소문자인지 확인한다.
2. 문자열에 따라 값을 처리하고 26으로 나눈 나머지를 더한다.
3. 새로운 문자열을 반환한다.
"""


def caesarCipher(s, k):
    mod = 26
    ret = ""

    for c in s:
        # check if c is lowercase
        if ord("a") <= ord(c) and ord(c) <= ord("z"):
            ret += chr(ord("a") + (ord(c) + k - ord("a")) % mod)

        # check if c is uppercase
        elif ord("A") <= ord(c) and ord(c) <= ord("Z"):
            ret += chr(ord("A") + (ord(c) + k - ord("A")) % mod)

        # rest
        else:
            ret += c

    return ret


s = "There's-a-starman-waiting-in-the-sky"
k = 3
print(caesarCipher(s, k))
