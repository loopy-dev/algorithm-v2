"""
Sparse Arrays
There is a collection of input strings and a collection of query strings. 
For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

input string이 있고, query string이 있다.
query string에 대해 얼마나 많이 보이는지 반환하자.
"""
"""
query string의 순서대로 몇 개가 있는지 구하는 것이다.
우선 query string을 순회하면서 해당 단어가 input string에 몇 개 있는지 확인한다. 이 작업은 O(N**2)시간이 소요된다.

1. input string에 대해 우선 dictionary화 한다. dictionary화를 통한 작업은 O(N)이다.
2. query string으로부터 get한다. 없다면 0을 가져온다.
3. 반환한다.
"""

def matchingStrings(strings, queries):
    counts = {}
    answer = [0] * len(queries)

    # add item into dictionary, counts
    for c in strings:
        counts[c] = counts.get(c, 0) + 1
    

    # count and fill answer
    for i in range(len(queries)):
        q = queries[i]
        answer[i] = counts.get(q, 0)
    
    return answer


strings = ['ab', 'ac', 'abc']
queries = ['ab', 'abc', 'bc']
print(matchingStrings(strings, queries))