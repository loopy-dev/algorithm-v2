"""
simple text editor
the editor initially contains an empty string S
perform Q operations of the following 4 types:

1. append(W) - append W to the end of S
2. delete(K) - Delete last K characters of S
3. print(K) - print the Kth character of S
4. undo - Undo the last operation of type 1 or 2

"""

import sys

si = sys.stdin.readline


def append(s, char):
    return s + char


def delete(s, index):
    return s[:(-index)]


def undo(s):
    last_operation = operations.pop()
    op = last_operation.split(" ")

    # append
    if op[0] == '2':
        s = append(s, op[1])

    # delete
    # 추가한 글자 수 만큼 삭제
    else:
        length = len(op[1])
        s = delete(s, length)

    return s


# operate 함수는 실제로 명령어가 들어왔을 때 실행될 함수
def operate(s, option_type, *args):
    if option_type == '1':
        s = append(s, args[0])
        operations.append(f'1 {args[0]}')

    elif option_type == '2':
        deleted = s[(-int(args[0])):]
        s = delete(s, int(args[0]))
        # operations에 추가한다
        operations.append(f'2 {deleted}')

    elif option_type == '3':
        print(s[int(args[0]) - 1])

    else:
        s = undo(s)

    return s


q = int(si())
s = ""
operations = []

for i in range(q):
    op = si().strip().split(" ")
    if len(op) > 1:
        s = operate(s, op[0], op[1])
    else:
        s = operate(s, op[0])
