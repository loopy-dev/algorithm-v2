# 미로 탈출
# 벽 -> 통과 X
# 통로만 통과 가능
# 미로를 빠져나가는 문 -> 오직 레버를 당겨서만 열 수 있음
# 출발지 -> 레버 -> 미로를 빠져나가는 문으로 이동
# 최대한 빠르게 미로를 빠져나가는데 걸리는 시간 구하기
# S: 시작 E: 출구 L: 레버 O: 통로 X: 벽
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

INF = 987654321


def bfs(sy, sx, ey, ex, maps):
    q = deque()

    visited = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q.append((sy, sx, 0))
    visited[sy][sx] = 0

    while q:
        y, x, cnt = q.popleft()

        if y == ey and x == ex:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= len(maps) or nx < 0 or nx >= len(maps[0]):
                continue

            if maps[ny][nx] == "X":
                continue

            if visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                q.append((ny, nx, cnt + 1))

    return visited[ey][ex]


def solution(maps):
    sy, sx, ly, lx, ey, ex = -1, -1, -1, -1, -1, -1

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                sy, sx = i, j
            elif maps[i][j] == "L":
                ly, lx = i, j
            elif maps[i][j] == "E":
                ey, ex = i, j
    distance1 = bfs(sy, sx, ly, lx, maps)
    distance2 = bfs(ly, lx, ey, ex, maps)
    return distance1 + distance2 if distance1 + distance2 < INF else -1


maps = ["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
print(solution(maps))
