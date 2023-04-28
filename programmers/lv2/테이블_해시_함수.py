def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    answer = 0
    
    for i in range(row_begin - 1, row_end):
        s = 0
        for j in range(len(data[0])):
            s += data[i][j] % (i + 1)

        answer ^= s

    return answer


data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
col = 2
row_begin = 2
row_end = 3
print(solution(data, col, row_begin, row_end))