## 210920

`<신규아이디추천>`

1. `new_id 모든 대문자 -> 소문자`

```python
    new_id = new_id.lower()
```

2. `new_id 알파벳, 소문자, 숫자, -, . 제외 모든 문자 제거`

```python
new_id = "".join(list(filter(lambda x: x.isalnum() or x == '-' or x == '_' or x == '.', new_id)))
```

> `x.isalnum()`: `x`가 _`알파벳`_ 이나 _`숫자`_ 라면 _`True`_ 반환, 아니라면 _`False`_ 반환

3. `new_id에서 (.)이 2번 이상 연속되면 하나의 (.)로 치환`

```python
new_id_stack = []
for id in new_id:
    if new_id_stack and id == '.' and new_id_stack[-1] == '.':
        continue
    new_id_stack.append(id)
new_id = "".join(new_id_stack)
```

4. `new_id에서 처음이나 마지막에 (.)가 있다면 제거`

```python
if new_id and new_id[0] == '.' : new_id = new_id[1:]
if new_id and new_id[-1] == '.' : new_id = new_id[:-1]
```

5. `new_id가 빈 문자열이라면 'a'대입`

```python
if not new_id: new_id = 'a'
```

6. `new_id의 길이가 16이상이면 15까지 끊기 + 4번`

```python
l = len(new_id)
if l >= 16:
    new_id = new_id[:15]
    if new_id[-1] == '.' : new_id = new_id[:-1]
```

7. `new_id의 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자 대입`

```python
elif l <= 2:
    new_id += new_id[-1] * (3 - l)
```

---

## 210921

`11055`
요즘 dp 점화식 세우는게 너무 어려워서 차근차근 실버부터 시작! ✨

1. `dp테이블을 입력받은 datas로 초기화 해준다.`

```
datas = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
dp = [1, 100, 2, 50, 60, 3, 5, 6, 7, 8]
```

2. `datas[i] (0 <= i <= len(datas))과 datas[j] (0 <= j <= i)를 돌면서 dp테이블 갱신`

```python
for i in range(l):
    for j in range(i, -1, -1):
        if datas[i] > datas[j]:
            dp[i] += dp[j]
            break
```

> TC만 보고 하다가 엣지 케이스를 생각못했다.
>
> > 위의 코드는 i번째에서 -1씩 감소 시켜서 datas[i]보다 작은 첫 datas[j]를 찾을 때 dp[i]를 종료한다.
> > 그런데 조건에 맞는 첫 j의 dp[j]보다 더 큰 dp[j]를 만족하는 j가 있을 가능성을 무시했다.

### 👇👇 고친 코드

```python
for i in range(l):
    now_d = dp[i]
    for j in range(i, -1, -1):
        if datas[i] > datas[j]:
            dp[i] = max(dp[i], now_d + dp[j])
```

> 모든 조건을 만족하는 j의 dp를 확인하면서 최댓값을 갱신해준다.

구글링안하고 직접 세운 점화식이어서 엄청 뿌듯🌈

---

## 210922

`<1912>`

경우는 두가지가 있다.

1. `앞의 숫자를 더하기`
2. `앞의 숫자를 더하지 않기`

```python
for i in range(1, l + 1):
    dp[i] = max(dp[i - 1] + datas[i - 1], datas[i - 1]) # 앞에꺼랑 더하거나, 안 더하거나
```

`<2156>`

처음 생각한 경우

```
Dp = [바로 다음과 더했을 때, 한 칸 뛰어넘고 더했을 때]
```

1. `바로 다음과 더하는 경우 (ex: idx = 0)`
   1. `idx = 1의 한 칸 뛰어넘고 더했을 때와 더한다.`
2. `한 칸 뛰어넘고 더하는 경우 (ex: idx = 0)`
   1. `idx = 2의 제일 최대값을 더한다.`

그런데 하나 빠뜨린게 있었다.

3. `현재 값을 선택 안하는 경우`

```python
for i in range(l - 1, -1, -1):
    dp[i][0] = max(dp[i + 1]) # 안먹기 -> 다음꺼의 max 선택 가능
    dp[i][1] = dp[i + 1][2] + datas[i] # 다음꺼 먹기 -> 다음꺼의 한칸 뛰어넘기만 선택
    dp[i][2] = max(dp[i + 2]) + datas[i] # 한칸 뛰어 먹기 -> 한칸 뛰어넘은거의 max 선택 가능
        result = max(result, max(dp[i]))
```

---

## 210924

`<2193>`

`10844`문제를 풀어 봐서 굉장히 쉬웠다.

`이친수`는 `0`, `1`로만 이루어져있다.

#### 조건

1. `0으로 시작 ❌`
2. `1이 연속으로 2번 이상 ❌`

조건 그대로 dp 점화식을 써 보면

```python
# dp[i][0]은 i자리의 뒷자리가 0인 경우 ex) i = 3 -> XX0인 숫자의 개수
# dp[i][1]은 i자리의 뒷자리가 1인 경우 ex) i = 3 -> XX1인 숫자의 개수
dp[0] = [0, 1] # 1
for i in range(1, n):
    # 0은 앞에 0, 1 뭐가 와도 상관 없음
    dp[i][0] = dp[i - 1][0] + dp[i - 1][1] # sum(dp[i - 1])
    # 1은 앞에 무조건 0이 와야 함
    dp[i][1] = dp[i - 1][0]
```

`<10844>`

_앞의 문제와 엄청 유사한 문제_

`dp[i][j]`는 i자리수의 마지막 숫자가 j - 1인 경우
`ex) dp[4][5] -> 4자리 수일 떄 마지막 숫자가 4인 경우`

#### 주의할 케이스

1. `끝자리가 0일때 -> 앞에 올 수 있는 수는 1 밖에 없음`
2. `끝자리가 9일때 -> 앞에 올 수 있는 수는 8 밖에 없음`

```python
dp = [[0] * 10 for _ in range(n)]
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(1, n):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
```

`<14501>`

처음 생각한 방법 (알고리즘에 부루트포스도 있길래)

```
# pseudo code
for i = 1 ~ n:
    t is time of data[i]
    p is profit of data[i]
    now_i is i
    sum is dp[i]'s max_profit
    while now_i < n:
        if i + t - 1 < n
            sum += p
            now_i += t - 1
        else:
            now_i++
    dp[i] = sum
```

이렇게 하면 중복되는 부분이 너무 많다. -> 지나갔던 부분을 여러번 지나게 된다.

그래서 topdown으로 다시 생각해보았다.

#### 경우

1. `지금꺼 선택 ❌`
2. `지금꺼 선택 ❌(가능하다면)`

```python
dp = [[0, 0] for _ in range(n + 1)] # 2차원으 풀 때
for i in range(n - 1, -1, -1):
    t, p = datas[i]
    if i + t <= n:
        # 가능하다면 현재 상담을 선택
        dp[i][1] = max(dp[i + t]) + p
    # 현재 상담 선택 안한다면 그 다음날 꺼 가능
    dp[i][0] = max(dp[i + 1])
```

그런데 이때 `dp[i][1]`과 `dp[i][0]`의 값을 정해주는 부분에서 모두 원하는 `dp`의 `max값`을 사용한다.

#### 이 말은 `max값 말고는 굳이 저정할 필요가 없다`는 뜻이다.

> `1차원`으로도 해결 가능하다.

```python
dp = [0] * (n + 1)
for i in range(n - 1, -1, -1):
    t, p = datas[i]
    dp[i] = dp[i + 1] if i + t > n else max(dp[i + 1], dp[i + t] + p)
```

---

## 210925

`<11052>`

사실 며칠 전에 슬쩍봤다가 어려워보여서 모른척했었던 문제다. 😂

오늘 이거는 제대로 푼다;; 하면서 계속 고민했다.

#### 결국 성공 👏

### `dp[i]는 카드를 (i + 1)개 집을 수 있을때의 max값이다.`

> 그럼 이때의 max값은 어떻게 구하나?
>
> 1. `dp[i] = max(dp[i], dp[k] + dp[i - k - 1]) (k = 0 ~ (i + 1) // 2)`
>    > 예를 들어 카드를 4개 집을 수 있을 때 가능한 경우는 `(1개 + 3개)`, `(2개, 2개)`이므로 `k`는 `1 ~ 2`까지 돌면서 `dp[k] + dp[i - k - 1]`와 `dp[i]`를 매번 비교해준다.

```python
dp = datas
for i in range(n):
    for j in range((i + 1) // 2):
        dp[i] = max(dp[i], dp[j] + dp[i - j - 1])
```

`<11057>`

이전에 풀었었던 문제랑 비슷한 문제

`dp[i][j]`는 `i자리 숫자`의 마지막 수가 `j`라는 뜻이다.

#### 주의할 케이스

1. `끝자리가 0일때 -> 앞에 0만 올 수 있음`

```python
dp[1] = [1] * 10
for i in range(2, n + 1):
    # dp[i][0]은 무조건 dp[i - 1][0]
    dp[i][0] = dp[i - 1][0]
    for j in range(1, 10): # 1 ~ 9까지 돌기
        # dp[i][j]는 dp[i - 1][0]부터 dp[i - 1][j]까지의 합이다.
        dp[i][j] = sum(dp[i -1][:j + 1])
```

---
