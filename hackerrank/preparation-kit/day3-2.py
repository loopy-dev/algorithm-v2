"""
Two players are playing a game of Tower Breakers! 
Player  always moves first, and both players always play optimally.
게임 이론 문제
n: tower 개수
m: 각 타워의 높이
플레이어는 각자의 턴에서 움직임
각 턴에서 플레이어는 높이가 x인 탑을 선택하고 높이를 y로 줄일 수 있음
이때, y는 x를 균등하게 나눈다.

매우 매우 어려운 문제였다. O(1)으로 접근해야만 풀 수 있는 문제로, 게임 이론에 대한 
이해가 필요하다.
"""
#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    # 첫 번째 턴을 base case로 잡는다.
    # 첫 번째 턴에 player1이 움직일 수 없다면, player 2의 승리다.
    if m == 1:
        return 2

    # 만약 움직일 수 있는 곳이 단 한 곳 밖에 남지 않는다면, player 1의 승리다.
    return 2 if n % 2 == 0 else 1
