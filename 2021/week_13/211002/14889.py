from itertools import combinations, permutations

def check_score(nums):
    sum = 0
    for i, j in permutations(nums, 2):
        sum += datas[i][j]
    return sum

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = [list(map(int, input().split())) for _ in range(n)]
    indexs = {i for i in range(n)}

    result = 201
    for index in combinations(range(n), n // 2):
        remain_indexs = indexs - set(index)
        result = min(result, abs(check_score(index) - check_score(remain_indexs)))
    print(result)