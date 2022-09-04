import heapq

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

INF = 987654321


def is_violating_social_distancing(visited, locations):
    for location in locations:
        y, x = location
        if visited[y][x] == 0:
            continue

        if visited[y][x] <= 2:
            return True

    return False


def dijkstra(sy, sx, visited, adj):
    q = []
    heapq.heappush(q, (0, sy, sx))
    visited[sy][sx] = 0
    while q:
        cnt, y, x = heapq.heappop(q)

        if visited[y][x] < cnt:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                continue

            if adj[ny][nx] == "X":
                continue

            if visited[ny][nx] > cnt + 1:
                visited[ny][nx] = cnt + 1
                heapq.heappush(q, (cnt + 1, ny, nx))


def get_peoples_location(place):
    ret = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                ret.append((i, j))
    return ret


def solution(places):
    answer = [1, 1, 1, 1, 1]
    for i in range(len(places)):
        place = places[i]
        locations = get_peoples_location(place)

        for location in locations:
            y, x = location
            visited = [[INF for _ in range(5)] for _ in range(5)]
            dijkstra(y, x, visited, place)

            if is_violating_social_distancing(visited, locations):
                answer[i] = 0
                break
    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

print(solution(places))
