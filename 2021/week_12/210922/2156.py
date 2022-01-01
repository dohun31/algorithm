if __name__ == "__main__":
    n = int(input())
    datas = [int(input()) for _ in range(n)]

    l = len(datas)
    dp = [[0, 0, 0] for _ in range(l + 2)]
    result = 0
    for i in range(l - 1, -1, -1):
        dp[i][0] = max(dp[i + 1]) # 안먹기 -> 다음꺼의 max 선택 가능
        dp[i][1] = dp[i + 1][2] + datas[i] # 다음꺼 먹기 -> 다음꺼의 한칸 뛰어넘기만 선택
        dp[i][2] = max(dp[i + 2]) + datas[i] # 한칸 뛰어 먹기 -> 한칸 뛰어넘은거의 max 선택 가능
        result = max(result, max(dp[i]))
    print(result)