# 7주차

> - Greedy
> - DP

---

## 21.08.16

> - [1003 - 피보나치 함수](https://www.acmicpc.net/problem/1003)
> - [1149 - RGB거리](https://www.acmicpc.net/problem/1149)
> - [1932 - 정수 삼각형](https://www.acmicpc.net/problem/1932)
> - [9095 - 1, 2, 3더하기](https://www.acmicpc.net/problem/9095)
> - [11726 - 2xN 타일링](https://www.acmicpc.net/problem/11726)

`<1003>`

첫 시도에 dp 말고 그냥 재귀로 했더니 `시간초과` 😢

```python
def fibonacci(n):
    if n == 0:
        zero_cnt += 1
        return 0
    elif n == 1:
        one_cnt += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

#### 👇👇 그래서 이렇게 바꿨다.

```python
def fibonacci(n):
    dp = [[1, 0], [0, 1]] # dp 기본 세팅
    if n > 1: # n이 2이상이면 bottom-up
        for i in range(2, n + 1):
            dp.append([dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1]]) # 행렬 덧셈 (dp[i - 2] + dp[ i - 1])
    return dp[n]
```

`<1149>`

갈팡 질팡하다가 결국엔 감잡으려고 구글링

```python
rgb[i][0] += min(rgb[i - 1][1], rgb[i - 1][2])
rgb[i][1] += min(rgb[i - 1][0], rgb[i - 1][2])
rgb[i][2] += min(rgb[i - 1][0], rgb[i - 1][1])
```

`<1932>`

보자마자 공책에 끄적끄적 해보고 바로 맞은 문제! 😀

```
7           7           7          7       30
3 8         3 8         3 8        23 21
8 1 0       8 1 0       20 13 10
2 7 4 4     7 12 6 10
4 5 2 6 5
```

`n - 1번째 행`부터 `0번째 행`까지 왼쪽자식, 오른쪽 자식 중에 최대의 자식을 선택에서 더하면서 올라간다.

```python
for i in range(1, n): # 좌, 우 중에 제일 큰값 더해서 올라가기
    for j in range(len(graph[i])):
        graph[i][j] += max(graph[i - 1][j], graph[i - 1][j + 1])
```

`<9095>`

1, 2, 3만 사용해서 n을 만드는 방법에는 `dp[i - 1] + 1`, `dp[i - 2] + 2`, `dp[i - 3] + 3`이 있다.

```python
def solution(n): # bottom-up
    dp = [0] * (n + 1)
    dp[:4] = [0, 1, 2, 4]
    if n > 3:
        for i in range(4, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] # i-1번쨰에서 '+1', i-2번째에서 '+2', i-3번째에서 '+3'
    return dp[n]
```

`<11726>`

타일 채우는 방법은 `dp[i - 1] + dp[i - 2]`이다.

> dp[i - 1] 은 2 \* 1 타일을 더하면 됨
> dp[i - 2] 는 1 \* 2을 위아래 붙여서 4 \* 4를 만든다
> ⚠️ dp[i - 2]에서 2 \* 1 두 개 붙여서 4 \* 4되는데 이건 왜 빼냐?
> 🔆 2 \* 1 쓰는 방법은 dp[i - 1]선에서 해결.(dp[i - 1]의 마지막 블럭이 2 \* 1이라면 방금 더한 2 \* 1이랑 합쳐져서 4 \* 4타일이 됨!)

---
