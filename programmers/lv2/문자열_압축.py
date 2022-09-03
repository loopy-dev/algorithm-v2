INF = 987654321


def solution(s):
    if len(s) <= 1:
        return len(s)
    answer = INF
    for i in range(1, len(s) // 2 + 1):
        idx = 0
        count = 0
        word = ""
        compacted = []
        while idx + i <= len(s):
            sliced = s[idx : idx + i]
            if sliced == word:
                count += 1
            else:
                compacted.append(str(count) + word if count > 1 else word)
                word = sliced
                count = 1
            idx += i
        compacted.append(str(count) + word if count > 1 else word)
        compacted.append(s[idx:])
        answer = min(answer, len("".join(compacted)))
    return answer


# s = "aabbaccc"
# s = "a"
# s = "aaaaaaaa"
# s = "aaaabbb"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
s = "xababcdcdababcdcd"
print(solution(s))
