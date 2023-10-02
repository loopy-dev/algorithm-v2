# pccp 모의고사 1번 - 외톨이 알파벳


def solution(input_string):
    answer = ""
    arr = [0] * 26
    prev = ""
    for c in input_string:
        if prev != c:
            prev = c
            arr[get_index(c)] += 1

    for i in range(26):
        if arr[i] > 1:
            answer += chr(i + ord("a"))

    return answer if answer else "N"


def get_index(c):
    return ord(c) - ord("a")


input_string = "zbzbz"
print(solution(input_string))
