"""
Palindrome index
"""
"""
팰린드롬을 위해 제거해야 할 문자를 확인
문자는 단 한번만 제거할 수 있다.

1. 팰린드롬을 확인하기 위하여 양 옆을 투 포인터로 확인할 수 있다.
2. 만약 두 글자가 다르다면 left, right를 빼보면서 팰린드롬이 가능한지 확인해본다.
3. 둘 다 안되거나 이미 팰린드롬이라면 -1을 반환한다.
"""


def check_is_palindrome(s, left, right):
    while left <= right:
        # check left is same with right
        if s[left] != s[right]:
            return [False, left, right]

        left += 1
        right -= 1

    return [True, left, right]


def palindromeIndex(s):
    left = 0
    right = len(s) - 1

    # check string is palindrome
    is_palindrome, left, right = check_is_palindrome(s, left, right)

    if is_palindrome:
        return -1

    is_palindrome, _, _ = check_is_palindrome(s, left + 1, right)

    if is_palindrome:
        return left

    is_palindrome, _, _ = check_is_palindrome(s, left, right - 1)

    if is_palindrome:
        return right

    return -1


s = "aaa"
print(palindromeIndex(s))
