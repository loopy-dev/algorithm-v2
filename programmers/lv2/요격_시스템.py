def solution(targets):
    targets.sort(key=lambda x: (x[0], x[1]))
    end_point = targets[0][1]
    answer = 1

    for i in range(1, len(targets)):
        s, e = targets[i]

        if s < end_point:
            if e < end_point:
                end_point = e
            continue

        answer += 1
        end_point = e

    return answer


targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))