def solution(arr, sum):
    if len(arr) == n:
        final_data = datas[arr[-1]][arr[0]]
        if final_data != 0:
            sum += final_data
            result.append(sum)
        return
    for idx, data in enumerate(datas[arr[-1]]):
        if data == 0:
            continue
        else:
            if idx not in arr:
                solution(arr + [idx], sum + data)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline

    n = int(input())
    datas = [list(map(int, input().split())) for _ in range(n)]

    result = []
    for i in range(n):
        for j in range(n):
            if i != j and datas[i][j] != 0:
                solution([i, j], datas[i][j])
    print(min(result))