## 210927

`<1915>`

가장 큰 정사각형을 찾아야 하는 문제.

`prefix sum`알고리즘밖에 생각이 안났다.

1. `prefix sum`구하기

```python
dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
 for i in range(1, row + 1):
    for j in range(1, col + 1):
        dp[i][j] += dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + datas[i - 1][j - 1]
```

2. `정사각형이 될 수 있는 최대의 변 길이 구하기`

```python
possible_l = min(row, col)
```

3. `1 ~ possilbe_l까지 정사각형이 있는지 찾기`

```python
for area in range(1, possible_l + 1):
    for i in range(area, row + 1):
        for j in range(area, col + 1):
            now_area = dp[i][j] - dp[i][j - area] - dp[i-area][j] + dp[i - area][j - area]
            if now_area == area * area:
                max_area = max(max_area, now_area)
```

`pypy3`를 써도 시간이 어마어마하게 걸린다.. 다른 방법도 찾아봐야겠다.

#### 그래도 직접 점화식 세워서 뿌듯🔆

---

## 210928

`<11054>`

`up_datas`: 원래 입력값
`down_datas`: 원래 입력값.`reverse()`

1. `up_datas`와 `down_datas`의 가장 긴 증가하는 부분 수열을 구함

```python
dp = [[1, 1] for _ in range(n)]
for i in range(n):
    for j in range(i):
        if up_datas[i] > up_datas[j]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        if down_datas[i] > down_datas[j]:
            dp[i][1] = max(dp[i][1], dp[j][1] + 1)
```

2. 가장 긴 바이토닉 수열을 구함.

```python
result = 0
for i in range(n):
    result = max(result, dp[i][0] + dp[n - 1 - i][1] - 1)
```

---
