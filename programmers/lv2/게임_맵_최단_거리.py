import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
INF = 987654321


def in_range(y, x, row, col):
    if y < 0 or y >= row or x < 0 or x >= col:
        return False
    return True


def dijkstra(sy, sx, visited, maps):
    q = []
    heapq.heappush(q, (1, sy, sx))
    visited[sy][sx] = 1

    while q:
        cnt, y, x = heapq.heappop(q)

        if cnt > visited[y][x]:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if not in_range(ny, nx, len(visited), len(visited[0])):
                continue

            if not maps[ny][nx]:
                continue

            if visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))


def solution(maps):
    visited = [[INF for _ in range(len(maps[0]))] for _ in range(len(maps))]
    dijkstra(0, 0, visited, maps)
    answer = visited[len(visited) - 1][len(visited[0]) - 1]
    return answer if answer < INF else -1


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1],
        [0, 0, 0, 0, 1]]

print(solution(maps))
