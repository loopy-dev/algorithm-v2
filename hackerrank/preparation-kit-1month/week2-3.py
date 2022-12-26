"""
Drawing Book
A teacher asks the class to open their books to a page number.
A student can either start turning pages 
from the front of the book or from the back of the book.
They always turn pages one at a time. When they open the book, 
page 1 is always on the right side:

When they flip page 1, they see pages 2 and 3. 
Each page except the last page will always be printed on both sides.
The last page may only be printed on the front, given the length of the book.
If the book is  pages long, and a student wants to turn to page p,
what is the minimum number of pages to turn?
They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages 
that must be turned in order to arrive at page p.
"""
"""
직관적으로 해결하기

가장 첫 페이지에서 시작하거나 가장 마지막 페이지에서만 책을 펼칠 수 있다.
1. 페이지는 0번부터 시작한다고 가정한다.
2. 페이지를 2개씩 끊었을 때, 찾으려는 페이지가 몇 번째 장에 위치하는지 확인한다.
3. 해당 페이지와 마지막장 - 해당 페이지의 값 중 작은 값을 반환한다.

example:
1 -> 0
2 -> 1
3 -> 1
4 -> 2
5 -> 2
6 -> 2

Time complexity: O(1)
"""


def pageCount(n, p):
    page = p // 2
    return min(page, (n // 2) - page)


n = 5
p = 3
print(pageCount(n, p))
