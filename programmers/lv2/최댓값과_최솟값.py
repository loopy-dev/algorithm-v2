def solution(s):
    arr = sorted(list(map(lambda x: int(x), s.split(' '))))
    return " ".join([str(arr[0]), str(arr[-1])])



s = "1 2 3 4"
print(solution(s))