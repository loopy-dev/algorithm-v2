"""
부대 복귀
강철 부대의 부대원이 여러 지역에 뿔뿔이 흩어져 특수 임무를 수행 중
지도에서 강철 부대가 위치한 지역을 포함한 각 지역은 유일한 번호로 구분됨
두 지역 간의 길을 통과하는데 걸리는 시간은 모두 1로 통일
단, 임무 시작 때와 다르게 되돌아오는 경로가 없어져 복귀가 불가능한 부대원도 존재

n: 총 지역의 수
roads: 두 지역을 왕복할 수 있는 길 정보를 담은 2차원 배열
sources: 각 부대원이 위치한 서로 다른 지역을 나타내는 정수 배열
destination: 강철부대의 지역

return: sources의 원소 순서대로 강철부대로 복귀할 수 있는 시간. 불가능할 경우 -1
"""
"""
1. 우선 adjacent array 정보가 필요 -> 배열 순회를 통해 왕복 그래프를 구성
2. destination으로부터 dfs 또는 bfs 진행 or dijkstra도 가능
2-1. dijkstra를 통해 destination으로부터 각 목적지까지 걸리는 거리 배열을 구하기
2-2. 초깃값은 INF로 실행
3. 가는데 걸리는 시간을 출력하면 됨, sources 배열의 원소를 출력, 순서대로

여기서는 dijkstra를 실행하는 방법을 이용하자
"""
import heapq

INF = 987654321


def dijkstra(start, adj, distance):
    """
    heap 자료구조를 이용하여 dijkstra 진행
    O(n*log(n)) 시간복잡도를 가짐
    """
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        # 메모된 거리가 dist보다 짧다면 더 이상 탐색할 필요가 없다.
        if distance[node] < dist:
            continue

        for nxt in adj[node]:
            nxt_distance = dist + 1

            if distance[nxt] > nxt_distance:
                distance[nxt] = nxt_distance
                heapq.heappush(q, (nxt_distance, nxt))


def solution(n, roads, sources, destination):
    adj = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    answer = []

    # create graph
    for a, b in roads:
        # 서로 왕복할 수 있어야 하므로 각 인덱스 모두 목적지를 넣어준다.
        adj[a].append(b)
        adj[b].append(a)

    # get distance array
    dijkstra(destination, adj, distance)

    # return value by sources
    for source in sources:
        value = distance[source]
        answer.append(value if value < INF else -1)

    return answer


n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5
print(solution(n, roads, sources, destination))
