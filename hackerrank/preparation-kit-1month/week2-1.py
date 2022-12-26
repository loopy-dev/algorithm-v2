"""
Sales By match
There is a large pile of socks that must be paired by color. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

색이 맞아 떨어져야만 하는 다수의 양말 켤레들이 있다.
각 양말의 색을 나타내는 배열이 있다. 
몇 켤레의 양말을 매칭시킬 수 있는지 결정해야 한다.
"""
"""
가장 직관적으로 해결하기

1. 모든 색의 개수를 센다.
2. 해당 색을 2로 나눈 몫을 취한다.

arr[i]의 범위가 1에서 100사이이기 때문에 카운팅 정렬을 이용한다. 
"""


def sockMerchant(n, arr):
    counts = [0] * 101
    answer = 0

    # iterate arr and count elements
    for i in range(n):
        index = arr[i]
        counts[index] += 1

    # add pair of colors
    for i in range(101):
        answer += counts[i] // 2

    return answer


n = 9
arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, arr))
