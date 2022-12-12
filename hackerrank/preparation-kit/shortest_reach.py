"""
BFS: shortest reach
"""
from collections import deque

INF = 987654321


def get_distance(graph, s):
    distance = [INF for _ in range(n + 1)]
    q = deque()
    q.append((s, 0))
    distance[s] = 0

    while q:
        node, dist = q.popleft()

        for nxt in graph[node]:
            if distance[nxt] < INF:
                continue

            distance[nxt] = dist + 1
            q.append((nxt, dist + 1))

    return distance


def bfs(n, m, edges, s):
    """
    n: number of nodes
    m: number of edges:
    edges: int[m][2] [start node, end node]
    s: starting node
    """
    graph = [[] for _ in range(n + 1)]

    # create graph
    for i in range(m):
        start, end = edges[i]
        graph[start].append(end)
        graph[end].append(start)

    return list(
        map(
            lambda x: 6 * x if x < INF else -1,
            filter(lambda x: x != 0, get_distance(graph, s)),
        ),
    )[1:]


q = int(input())
for _ in range(q):
    n, m = list(map(int, input().split(" ")))

    edges = []

    for _ in range(m):
        a, b = list(map(int, input().split(" ")))
        edges.append([a, b])

    s = int(input())

    result = bfs(n, m, edges, s)
    print(result)
