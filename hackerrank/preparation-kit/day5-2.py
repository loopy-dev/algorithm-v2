"""
A queue is an abstract data type that maintains the order in which elements were added to it, 
allowing the oldest elements to be removed from the front and new elements to be added to the rear. 
This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue 
(i.e., the one that has been waiting the longest) is always the first one to be removed.
"""
"""
In this challenge, you must first implement a queue using two stacks. Then process q queries,
"""
"""
stack 2개로 queue 구현하기
inbox와 outbox로 구성
inbox = [1, 2, 3, 4]
outbox = [4, 3, 2, 1] -> pop
inbox = [5, 6, 7, 8]
outbox = [4, 3, 2, 1]
"""


class Queue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if self.outbox:
            return self.outbox.pop()

        while self.inbox:
            self.outbox.append(self.inbox.pop())

        return self.outbox.pop()

    def front(self):
        if self.outbox:
            return self.outbox[-1]

        return self.inbox[0]


q = int(input())
queue = Queue()
for _ in range(q):
    lst = list(map(int, input().split(" ")))

    # enqueue
    if lst[0] == 1:
        number = lst[1]
        queue.enqueue(number)

    # dequeue
    elif lst[0] == 2:
        queue.dequeue()

    # print
    else:
        print(queue.front())
