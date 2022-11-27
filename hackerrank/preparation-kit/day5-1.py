"""
Merge two sorted linked lists
두 유사 배열을 합치는 방법은 merge sort의 merge를 이용하는 것이 좋겠다.
그 이유는 이미 두 배열은 정렬되어 있는 형태이기 때문에 merge 과정을 통해
하나의 배열로 합칠 수 있기 때문이다.
"""
import math
import os
import random
import re
import sys

sys.stdin = open("../../cases/day5-1.txt", "r")
si = sys.stdin.readline


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node  # type: ignore

        self.tail = node


def print_singly_linked_list(node):
    while node:

        print(node.data, end=" ")

        node = node.next


def mergeLists(head1, head2):
    ret = SinglyLinkedList()
    left = head1
    right = head2

    while left and right:
        while left and right and left.data <= right.data:
            ret.insert_node(left.data)
            left = left.next

        while left and right and left.data > right.data:
            ret.insert_node(right.data)
            right = right.next

    while left:
        ret.insert_node(left.data)
        left = left.next

    while right:
        ret.insert_node(right.data)
        right = right.next

    return ret.head


t = int(si().strip())

for _ in range(t):
    n1 = int(si().strip())

    list_1 = SinglyLinkedList()

    for _ in range(n1):
        list_1.insert_node(int(si().strip()))

    n2 = int(si().strip())

    list_2 = SinglyLinkedList()

    for _ in range(n2):
        list_2.insert_node(int(si().strip()))

    list_3 = mergeLists(list_1.head, list_2.head)

    print_singly_linked_list(list_3)
    print()
