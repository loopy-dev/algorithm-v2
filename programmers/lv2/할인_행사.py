"""
할인 행사
XYZ 마트에서는 일정한 금액을 지불하면 10일 동안 회원 자격을 부여한다.
매일 회원을 대상으로 한 가지 제품에 대해 할인 행사를 진행한다.
할인하는 제품은 하루에 하나만 구매할 수 있다.
모든 제품을 할인받을 수 있는 회원 등록 날짜의 수를 구한다.

number의 원소 총 합은 10이다.

1. 구간을 처음에 더하고, 투 포인터를 이용하여 한 칸씩 이동할 때마다 왼쪽 물품을 하나 빼고
오른쪽 물품을 하나 더한다.
2. 모든 물품의 수량과 처음 주어진 배열의 수량과 동일한지 확인한다.
3. 동일하다면 answer를 1 더한다.
"""
def add_discount_day(shopping_list, current):
    for product in current.keys():
        if current.get(product, 0) != shopping_list.get(product, 0):
            return 0
    
    return 1

def solution(want, number, discount):
    answer = 0
    
    # want, number에 대하여 우선 딕셔너리를 만들어 빠르게 탐색할 수 있도록 한다.
    shopping_list = {}

    for i in range(len(want)):
        product = want[i]
        count = number[i]
        shopping_list[product] = count
    
    # 구간을 처음 더하기 전 초기화
    current = {}
    for i in range(sum(number)):
        product = discount[i]
        current[product] = current.get(product, 0) + 1

    left = 0
    right = sum(number)

    # 구간 탐색
    while right < len(discount):
        answer += add_discount_day(shopping_list, current)

        left_product = discount[left]
        right_product = discount[right]
        current[left_product] = current.get(left_product, 0) - 1
        current[right_product] = current.get(right_product, 0) + 1

        left += 1
        right += 1
    
    # 마지막 처리
    answer += add_discount_day(shopping_list, current)

    return answer