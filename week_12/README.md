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
