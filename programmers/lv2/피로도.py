def backtrack(fatigue, idx, visited, dungeons):
    if fatigue - dungeons[idx][0] < 0:
        return 0

    # 각 지점에 방문했을 때 최댓값을 저장한다.
    answer = 0
    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = True
            answer = max(
                answer,
                backtrack(fatigue - dungeons[idx][1], i, visited, dungeons))
            visited[i] = False

    return answer + 1


# 순서에 따라 달라질 수도 있다. -> backtracking으로 점근해야 한다.
# 각 던전은 하루에 한 번만 탐험할 수 있다.
# visited 배열이 있어야, 이미 방문한 지점을 방문하지 않는다.
def solution(k, dungeons):
    answer = 0

    for i in range(len(dungeons)):
        visited = [False] * len(dungeons)
        visited[i] = True
        ret = backtrack(k, i, visited, dungeons)
        answer = max(answer, ret)

    return answer


k = 80
dungeons = [[80, 20], [50, 40], [30, 10]]
print(solution(k, dungeons))
