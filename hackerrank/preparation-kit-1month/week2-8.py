"""
Grid Challenge
column 역시 ascending으로 배치가 되어 있다면 YES
아니면 NO 출력
"""
"""
row: 이미 정렬이 되어 있음, 위치 이동 불가
col: 체크 필요
same row에 있는 문자열들은 정렬이 가능하다

1. 1차원 배열에서 인덱스를 통해 각 배열의 ord를 확인한다.(단순 문자열로 비교도 가능)
1-1. 우선 row 문자열을 정렬한다.
2. 만약 저장한 문자열보다 작다면 False를 반환
3. 아니면 True를 반환한다.

Test case 100
n = 100
n * n = 1만 이므로 주어진 시간 내에 해결은 가능하다.
"""


def check(grid):
    for j in range(len(grid[0])):
        last_chr = ""

        for i in range(len(grid)):
            # return False if current chr is smaller than stored
            if grid[i][j] < last_chr:
                return False

            last_chr = grid[i][j]

    return True


def gridChallenge(grid):
    matrix = []

    # create matrix and sort
    for c in grid:
        arr = list(c)
        arr.sort()
        matrix.append(arr)

    return "YES" if check(matrix) else "NO"


grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
print(gridChallenge(grid))
