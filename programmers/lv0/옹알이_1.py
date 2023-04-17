words = ["aya", "ye", "woo", "ma"]


# babbling의 각 문자열에서 aya ye woo ma는 각각 최대 1번씩만 등장한다.
# 해당 문자열을 순회하면서 조건을 만족하면 True, 그렇지 않다면 False를 반환하고 그 개수를 센다.
def can_say_a(word):
    idx = 0

    while idx < len(word):
        flag = False

        for w in words:
            nxt_idx = idx + len(w)
            if word[idx:nxt_idx] == w:
                flag = True
                idx = nxt_idx
                break

        if not flag:
            return False

    return True


def solution(babbling):
    answer = len(list(filter(can_say_a, babbling)))
    return answer


babbling = ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
print(solution(babbling))
