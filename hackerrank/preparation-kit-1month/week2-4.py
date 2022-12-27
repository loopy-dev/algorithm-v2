"""
Tower Breakers
Two players are playing a game of Tower Breakers!
Player 1 always moves first, and both players always play optimally.
The rules of the game are as follows:

게임 이론 적용
항상 player 1이 먼저 시작하며 최선의 플레이를 한다.
- n개의 타워가 있다.
- 모든 타워의 높이는 m이다.
- 움직일 수 없다면 해당 플레이어는 진다.
플레이어 1이 이긴다면 1을 반환하고 플레이어 2가 이긴다면 2를 반환한다.
"""
"""
더 이상 움직일 수 없는 경우는 언제인가? 최소 한 칸은 남겨야 하기 때문에
타워의 높이가 1이라면 더 이상 진행할 수 없다.
1. m == 1일 경우, 플레이어 2가 승리한다.

그리고, 한 번에 하나의 타워만 컨트롤 할 수 있다. 이때 타워의 높이는 상관이 없다.
어떻게든 1을 만들면 무조건 성공하기 때문이다. 6 % 1 = 0, 5 % 1 = 0
따라서 타워의 개수가 홀수 -> 플레이어 2가 움직일 수 없으므로 1 승
타워의 개수가 짝수 -> 플레이어 1이 움직일 수 없으므로 2 승
"""


def towerBreakers(n, m):
    if m == 1:
        return 2

    return 1 if n % 2 == 1 else 2


n = 2
m = 6
print(towerBreakers(n, m))
