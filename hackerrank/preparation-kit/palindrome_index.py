"""
Given a string of lowercase letters in the range ascii[a-z]
determine the index of a character that can be removed to make the string a palindrome
If the word is already palindrome or there is no solution: return -1
"""
"""
1. palindrome인지 확인 -> palindrome이라면 return -1
2. 순서대로 한 글자씩 대체하면서 확인 -> 나머지에 대해 palindrome인지 확인
> 시간 초과
> 2차원 dp로도 시간 초과가 발생할 것

abcde
abcde

# 홀수일 경우
abdedcdba



1. 양쪽 끝 문자열 부터 좁혀가면서 확인한다.
2. 양쪽 끝 문자열이 다르다면, 양 쪽 문자열 중 하나를 제거하아고 난 뒤 팰린드롬인지 확인한다.

최적화 하는 방법이 너무 어렵다!!
"""


def palindromeIndex(s):
    # Write your code here.
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            break
        left += 1
        right -= 1

    if left >= right:
        return -1

    # left 제외, right 제외 확인
    # left
    f_left = left + 1
    f_right = right
    is_palindrome = True

    while f_left < f_right:
        if s[f_left] == s[f_right]:
            f_left += 1
            f_right -= 1
        else:
            is_palindrome = False
            break

    if is_palindrome:
        return left

    l_left = left
    l_right = right - 1
    is_palindrome = True

    while l_left < l_right:
        if s[l_left] == s[l_right]:
            l_left += 1
            l_right -= 1
        else:
            is_palindrome = False
            break

    if is_palindrome:
        return right

    return -1


s = "baa"
print(palindromeIndex(s))
