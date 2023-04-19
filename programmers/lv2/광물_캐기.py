# 사용할 수 있는 곡갱이중 아무거나 하나를 선택해 광물을 캔다.
# 한번 사용하기 시작한 곡갱이는 사용할 수 없을 때까지 사용한다.
# 광물은 주어진 순서대로만 캘 수 있다.
# 모든 광물을 캐거나 더 사용할 곡갱이가 없을 때까지 광물을 캔다.
# 한 곡갱이는 광물 5개만을 캘 수 있다.

# picks: 곡갱이의 개수, [dia, iron, stone]
# minerals: 광물 순서 [diamond, iron, stone]
# returns: 최소한의 피로도


def add_weight(picks):
    ret = []
    s = []
    for i in range(len(picks)):
        if i % 5 == 0 and s:
            ret.append(s)
            s = []

        if picks[i] == "diamond":
            s.append(25)
        elif picks[i] == "iron":
            s.append(5)
        else:
            s.append(1)

    ret.append(s)

    return ret


def make_picks_arr(picks):
    arr = []
    for i in range(len(picks)):
        for _ in range(picks[i]):
            arr.append(5 ** (2 - i))

    return arr


def solution(picks, minerals):
    answer = 0

    # 가중치 부여 -> 가중치는 diamond: 25, iron: 5, stone: 1
    picks_arr = make_picks_arr(picks)
    _weights = add_weight(minerals)
    weights = _weights[: len(picks_arr)]
    weights.sort(key=lambda x: -sum(x))

    for i in range(min(len(weights), len(picks_arr))):
        for j in range(len(weights[i])):
            answer += max(weights[i][j] // picks_arr[i], 1)
    # 문자 -> 숫자
    return answer


picks = [0, 1, 1]
minerals = [
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "diamond",
    "iron",
    "iron",
    "iron",
    "iron",
    "iron",
    "diamond",
]
print(solution(picks, minerals))
