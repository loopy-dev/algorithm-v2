"""
No Prefix set

문자열 배열이 주어지고, 각 문자열은 a부터 j까지의 소문자를 포함하고 있다.
문자열이 다른 문자열의 prefix가 되는 문자열이 하나도 없다면 GOOD SET을 출력한다.
그렇지 않다면 BAD SET과 문제가 되는 해당 문자열을 출력한다.

조건:
n: 문자열 배열 길이, 최대 1만개
words[i]: 최대 60
"""
"""
우선 무식하게 접근하기(실패)
1. 문자열을 정렬한다. 문자열 정렬시 아스키 순서대로 정렬되며 같은 아스키라면 길이가 긴 문자열이
뒤로 배치된다.
2. prev와 current의 문자열을 비교한다. prev와 current[:len(prev)]가 서로 동일하다면 prefix 조건을 만족하는 것이다.

테스트는 입력 순서대로 확인해야 하므로, 다른 방법이 필요하다.

```python
# example
arr = ["abc", "ab", "a"]
arr.sort()
print(arr) # ['a', 'ab', 'abc']
```
"""
"""
d -> d 하나가 저 뒤의 문자열과도 비교할 수 있게 해야 하므로, 다른 방법이 필요
Trie 자료 구조 활용
"""
import sys

sys.stdin = open("../../cases/day7-3.txt", "r")
si = sys.stdin.readline

# INF = 987654321


# def check(words):
#     """
#     check if word is prefix of other words.
#     return index
#     """
#     min_idx = INF
#     arr = []

#     for i in range(len(words)):
#         arr.append((words[i], i))

#     arr.sort(key=lambda x: (x[0], x[1]))

#     print(arr)

#     for i in range(1, len(arr)):
#         prev, _ = arr[i - 1][0], arr[i - 1][1]
#         current, current_idx = arr[i][0], arr[i][1]

#         if prev == current[: len(prev)]:
#             min_idx = min(min_idx, current_idx)

#     return min_idx


# def noPrefix(words):
#     result = check(words)
#     if result == INF:
#         print("GOOD SET")
#         return

#     print("BAD SET")
#     print(words[result])


def noPrefix(words):
    prefix_set = set()
    word_set = set()
    for w in words:
        check = ""
        if w in prefix_set:
            print("BAD SET")
            print(w)
            return
        for l in w:
            check += l
            prefix_set.add(check)
            if check in word_set:
                print("BAD SET")
                print(w)
                return
        word_set.add(w)
    print("GOOD SET")


t = int(si())
words = []
for _ in range(t):
    word = si().strip()

    words.append(word)

noPrefix(words)
