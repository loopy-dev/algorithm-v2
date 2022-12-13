"""
Huffman decoding
허프만 코딩은 가변 길이의 코드를 고정된 길이의 input의 글자의 빈도에 따라 할당한다.
가장 빈도수가 높은 character는 짧은 코드가 할당되고, 빈도수가 낮은 character일수록
긴 코드가 할당된다.
문자 경로를 따라 있는 모든 가장자리에는 코드 숫자가 포함되어 있다.
만약 노드가 트리에서 부모 노드의 왼쪽 자식이라면, 부모 노드와 왼쪽 노드 간 edge의 값은 0이 된다.
만약 노드가 부모 노드의 오른쪽 자식이라면, 부모 노드와 오른쪽 노드 간 edge의 값은 1이 된다.
리프 노드에만 에만 문자와 빈도 수가 포함된다.
다른 모든 노드에는 문자 대신 null이 포함되며 모든 노드와 해당 하위 문자의 빈도 수가 포함된다.
"""
"""
무식하게 풀어보기
1. `huffman_hidden` 이라는 함수는 정확하게 무엇을 하는지 알 수 없으나, 트리를 반환하는 함수이다.
2. 따라서 트리와 함께 dfs를 해주면 된다.

1. dfs를 통해 root에서부터 자식 노드로 탐색을 진행한다.
2. 방문함과 동시에 visited index 배열을 방문 처리하여, 이미 방문한 인덱스를 탐색하지 않도록 한다.
3. dfs로 순회하면서 해당 인덱스를 방문처리한다. 또한, 자식노드가 존재하는지, 존재하지 않는지 여부를 탐색한다.
4. 자식 노드가 있고 다음 인덱스의 글자와 동일하다면 탐색을 진행하고, 그렇지 않다면 탐색을 종료한다.
"""
"""
class Node:
    def __init__(self, freq, data):
        self.freq = freq
        self.data = data
        self.left = None
        self.right = None
"""


def dfs(node, string, visited, idx):
    if not node.left and not node.right:
        return node.data

    if not node.left and string[idx] == "0":
        return node.data

    if not node.right and string[idx] == "1":
        return node.data

    visited[idx] = True

    ret = ""
    if string[idx] == "0":
        ret = dfs(node.left, string, visited, idx + 1)

    else:
        ret = dfs(node.right, string, visited, idx + 1)
    return ret


def decodeHuff(root, s):
    visited = [False] * len(s)
    string = ""

    for i in range(len(s)):
        if not visited[i]:
            string += dfs(root, s, visited, i)

    print(string)
