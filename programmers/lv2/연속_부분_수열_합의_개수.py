"""
연속 부분 수열 합의 개수
1. 각 길이에 따라 부분 수열의 합을 구한다.
2. 연속된 합을 구하기 위하여 미리 부분합을 구한다.
"""

def partial_sum(elements):
    s = 0
    arr = [0]

    for i in range(len(elements)):
        s += elements[i]
        arr.append(s)
    
    return arr

def solution(elements):
    s = set()
    arr = elements[:] + elements[:]

    # psum[1] - psum[1] = 0, psum[1] - psum[0] = 7
    psum = partial_sum(arr)

    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            # save value into set
            current_sum = psum[j + i] - psum[j]
            s.add(current_sum)
    return len(s)


elements = [7, 9, 1, 1, 4]
print(solution(elements))