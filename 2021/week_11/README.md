## 210913

`<19551>`
카카오 코테 6번에 나온거랑 비슷한 문제.

`광고삽입`문제에서 광고가 시작될 때 1, 끝날때 -1을 사용해서 1 + (-1) = 0이 되게 하는 방법을 여기서 사용했다.

예를들어 1 5 -3이면, 1~5번째까지 -3을 해줘라니까 다음과 같이 코드를 작성하면 된다.

```python
start, end, d = 1, 5, -3
dp[start] += d
dp[end + 1] -= d
```

이때 `end`까지 하면 1 ~ 4까지 밖에 안되기 때문에, `end + 1`라고 선언을 해주어야 한다.

걱정한게 case(N)의 `end + 1`과 case(K)의 `start`가 겹치면 어쩌지 걱정을 했지만 결국엔 상쇄가 돼서 괜찮다.

```python
# case1: 1, 5, -3, case2: 6, 10, 5

# 1번쨰) data 입력받기
for _ in range(m):
    start, end, d = map(int, input().split())
    dp[start] += d
    dp[end + 1] -= d
# dp = [-3, 0, 0, 0, 0, (3 + 5), 0, 0, 0, 0, -5]

#2번째) 가중치들 구하기
for i in range(1, n + 1):
    dp[i] += dp[i - 1]
# dp = [-3, -3, -3, -3, -3, 5, 5, 5, 5, 5, 0]
```

짜잔🌟

`광고삽입`

문제 어떻게 풀지는 다 정했는데 진짜 아까운 문제

#### `내가 생각한 것(구글링 x)`

1. `시작할때 +1, 끝날때 -1해서 상쇄 처리 하기`
2. `누적합 해서 광고 누적 개수 구하기`
3. `투 포인터로 광고 시간 넘을 때 max_time, max_cnt 갱신하기`

### `내가 놓친 것(구글링)`

##### 1. `받은 logs로만 구하려고 해서 오류가 남`

1.  `구해야하는건 광고 시간을 다 채웠을 떄(초 단위)`
2.  `내가 구한건 광고 단위`
3.  `광고 시작과 끝 시간에 종속적이었음.`

##### 2. `완전 탐색 가능하다..!!!`

1.  `99시간 59분 59초가 제한이니까 충분히 할 수 있다.`

정말 공부를 많이 해야겠다.

---

## 210914

`카카오 6번`

풀었다!!

13일에 풀었던 `19551`을 미리 알았다면 이 문제를 푸는데 10분도 안걸릴만큼 쉬운 문제이다.

먼저 skill 쿼리들을 돌면서 스킬을 적용한다.

```python
def apply_skill(r1, c1, r2, c2, d):
        dp[r1][c1] -= d
        dp[r2 + 1][c1] += d
        dp[r1][c2 + 1] += d
        dp[r2 + 1][c2 + 1] -= d

for type, r1, c1, r2, c2, degree in skill:
    if type == 2: degree = -degree
        apply_skill(r1 + 1, c1 + 1, r2 + 1, c2 + 1, degree)
```

이때 스킬들의 `degree`는 원하는 사각형에 기록해두는데 이때 중요한건 `왼쪽 위`, `오른쪽 위 + 1`, `왼쪽 아래 + 1`, `오른쪽 아래 + 1`순서대로 `d`, `-d`, `-d`, `d`가 되게 해주어야 한다.

##### _이렇게 하면 서로 서로 상쇄가 되어서 원하는 부분에만 `degree`만큼 적용이 된다._

그리고 `bottom-up`방식으로 `dp`테이블을 채워주면서 바로바로 결과를 갱신해주면 된다.

```python
cnt = 0
for i in range(1, row + 1):
    for j in range(1, col + 1):
        dp[i][j] += dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
        if board[i - 1][j - 1] + dp[i][j] > 0: cnt += 1
```

#### `O(S + R*C) (S = len(skills), R = len(row), C = len(col))`

---

## 210915

`9663`

정말 정말 유명한 `N-Queen`문제.

이번 카카오 코테 치면서 `백트래킹`, `완탐` 연습해야 할 것 같아서 풀게 되었다.

일단 `백트래킹`이 잘 와닿지 않았는데 꾸역꾸역 머리에 넣고는 있다..

차근차근 보자면

1. `모든 열을 탐색한다.`

```python
 # 모든 열 탐색
for col in range(n):
    queens[row] = col
```

2. `모든 행을 탐색하면서 가능한 열을 구한다.`

```python
for x in range(row):
    # 같은 열에 있다면
    if queens[x] == queens[row]:
        break
    # 대각선에 있다면
    if abs(queens[x] - queens[row]) == (row - x):
        break
else:
    count += dfs(queens, n, row + 1)
```

> for-else문을 알게되었다.
> 항상 for문을 사용할 때 탈출 문은 잘 썼다. 그런데 걸러지지 않은 애들은 flag나, cnt로 처리했는데 for-else문이 있었다니.. 정말 좋은 문법이다.

`1759`

_`조건: 사전순, 길이가 l, 자음 2개이상, 모음 1개이상 포함된 단어`_

1. `알파벳들을 정렬하고 처음부터 차례대로 시작한다.`

```python
alpha = sorted(list(input().split()))
 for i in range(c):
    m = j = 0 # 모음, 자음
    if alpha[i] in m_um: m += 1
    else: j += 1
    make_word(alpha[i], l, c, i, m, j)
```

2. `원하는 길이가 됐을때 조건을 만족하면 출력하기`

```python
if len(word) == l and m >= 1 and j >= 2:
    print(word)
    return
```

3. `길이가 오버됐다면 끝내기`

```python
if len(word) > l:
    return
```

4. `2번이나 3번을 만족할 때 까지 word를 불려가면서 가능한 word 찾기`

```python
for i in range(idx + 1, c):
    # 모음개수, 자음개수 copy하기
    M, J = m, j
    if alpha[i] in m_um: M += 1
    else: J += 1
    make_word(word + alpha[i], l, c, i, M, J)
```

> M, J 변수 두고 m, j copy한 이유
>
> > Copy하지 않으면 for문 돌면서 m, j가 점점 증가 -> 매 케이스마다 독립적이지 않게 됨.

---
