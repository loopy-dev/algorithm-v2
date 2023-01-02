"""
혼자 놀기의 달인

숫자 카드 더미에는 카드가 총 100장 존재한다.
각 카드에는 1부터 100까지 숫자가 하나씩 적혀있다.
2이상 100이하의 자연수를 하나 정해 그 수보다 작거나 같은 숫자 카드들을 준비한다.
준비한 카드의 수만큼 작은 상자를 준비하면 게임을 시작할 수 있다.

상자에 카드를 한 장씩 넣어 상자를 무작위로 섞은다음 오름차순으로 번호를 붙인다.
임의의 상자를 열어 숫자 카드를 확인한다.
확인한 카드에 적힌 번호에 해당하는 상자를 열어 안에 담긴 카드에 적힌 숫자를 확인한다.
확인한 카드에 적힌 번호에 해당한느 상자를 열고 이를 반복한다. 열어야 하는 상자가 이미 열려있을 때까지 반복한다.

이렇게 연 상자들은 1번 상자 그룹이다. 1번 상자 그룹을 제외하고 남는 상자가 없으면 게임이 종료되고
얻는 점수는 0점이다.

남은 상자를 다시 같은 방식으로 연다. 
1번 그룹 상자의 수 * 2번 그룹 상자의 수가 점수가된다.

얻을 수 있는 최고 점수: 1번 그룹 상자의 수 == 2번 그룹 상자의 수
차이가 적을 수록 얻을 수 있는 점수는 높아진다.
"""
"""
어떤 상자를 먼저 여는지에 따라 그룹이 달라지기 때문에 모든 상자에 대해 실시해야 한다.
탐색 시간은 O(N)이므로 O(N ** 2)까지는 괜찮다. 왜냐하면 상자의 개수는 최대 100개이기 때문이다.
어떤 지점에서 시작하더라도 방문 순서는 동일하므로 한 번만 방문하면 된다.

1. 각 지점에 대해 dfs를 실시한다. dfs를 위하여 visited[number] 배열을 선언하여 그룹을 만든다.
2. n개의 그룹 결과가 나오기 때문에 정렬하여 가장 높은 것 두 개를 선택하여 곱하면 된다.
"""

def dfs(node, visited, cards, group):
    if visited[node]:
        return
    
    visited[node] = group
    dfs(cards[node], visited, cards, group)


def solution(cards):
    # index와 요소를 일치시키기 위하여
    cards = list(map(lambda x: x - 1, cards))
    visited = [0] * len(cards)
    group = 1

    for i in range(len(cards)):
        if not visited[i]:
            dfs(cards[i], visited, cards, group)
            group += 1
    
    counts = [0] * (max(visited) + 1)
    
    for i in range(len(visited)):
        counts[visited[i]] += 1

    counts.sort()

    return counts[-1] * counts[-2]
