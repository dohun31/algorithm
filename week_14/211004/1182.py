def solution(cnt, now_sum):
    if cnt == n:
        if now_sum == s: return 1
        else: return 0
    return solution(cnt + 1, now_sum + datas[cnt]) + solution(cnt + 1, now_sum)

if __name__ == "__main__":
    n, s = map(int, input().split())
    datas = list(map(int, input().split()))
    result = solution(0, 0)
    print(result if s != 0 else result - 1)