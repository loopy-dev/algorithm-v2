def solve(arr):
    ret = []
    for i in range(len(arr)):
        if not arr[i]:
            ret.append(i)

    return ret


students = [False for _ in range(30)]

for i in range(28):
    number = int(input())
    students[number - 1] = True

print("\n".join(list(map(str, map(lambda x: x + 1, solve(students))))))
