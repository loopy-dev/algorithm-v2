from collections import deque

INF = 987654321


def get_abs(side, n):
    return abs(2 * side - n)


def bfs(start, disabled_a, disabled_b, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()

        for nxt in graph[node]:
            if nxt == disabled_a or nxt == disabled_b:
                continue

            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)


def get_adj(n, wires):
    ret = [[] for _ in range(n + 1)]
    for a, b in wires:
        ret[a].append(b)
        ret[b].append(a)
    return ret


def solution(n, wires):
    result = INF
    graph = get_adj(n, wires)

    for a, b in wires:
        # 한 쪽을 구하면 나머지 한 쪽은 자동으로 계산된다.
        visited = [False] * (n + 1)
        for i in range(1, n + 1):
            if not visited[i]:
                bfs(i, a, b, graph, visited)
                break

        result = min(result, get_abs(len(list(filter(lambda x: x, visited))),
                                     n))

    return result
