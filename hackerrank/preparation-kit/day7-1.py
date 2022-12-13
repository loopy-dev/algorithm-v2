"""
preorder tranversal
"""


class Node:
    def __init__(self, info) -> None:
        self.info = info
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return self.info


def preOrder(root):
    print(root.info, end=" ")

    if root.left:
        preOrder(root.left)

    if root.right:
        preOrder(root.right)
