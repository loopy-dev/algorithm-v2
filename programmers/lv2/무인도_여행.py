from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def create_map(maps):
    return list(
        map(
            lambda x: list(map(lambda y: int(y)
                               if y.isdigit() else y, list(x))), maps))


def bfs(sy, sx, maps, visited):
    q = deque()
    visited[sy][sx] = True
    ret = maps[sy][sx]
    q.append((sy, sx))

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(maps) or nx < 0 or nx >= len(maps[0]):
                continue

            if maps[ny][nx] == 'X':
                continue

            if not visited[ny][nx]:
                visited[ny][nx] = True
                ret += maps[ny][nx]
                q.append((ny, nx))

    return ret


def solution(maps):
    # 맵 만들기
    answer = []
    adj = create_map(maps)
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    # bfs를 통해 각 단면적 구하기
    for i in range(len(adj)):
        for j in range(len(adj[0])):
            if maps[i][j] == 'X':
                continue

            if not visited[i][j]:
                cnt = bfs(i, j, adj, visited)
                answer.append(cnt)

    if not answer:
        answer.append(-1)
        return answer

    answer.sort()
    return answer


maps = ["XXX","XXX","XXX"]
print(solution(maps))