import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    dp = [[0] * 2] * n

    if n == 1:
        datas = int(sys.stdin.readline())
        print(datas, datas)
    else:
        for i in range(n):
            datas = list(map(int, sys.stdin.readline().split()))
            nowv = [[datas[k]] * 2 for k in range(n)]
            for j in range(n):
                if j == 0:
                    nowv[j][0] += max(dp[j][0], dp[j + 1][0])
                    nowv[j][1] += min(dp[j][1], dp[j + 1][1])
                elif j == n - 1:
                    nowv[j][0] += max(dp[j][0], dp[j - 1][0])
                    nowv[j][1] += min(dp[j][1], dp[j - 1][1])
                else:
                    nowv[j][0] += max(dp[j - 1][0], dp[j][0], dp[j + 1][0])
                    nowv[j][1] += min(dp[j - 1][1], dp[j][1], dp[j + 1][1])
            dp = nowv

        print(max(dp)[0], min(dp)[1])