## 01월 01일

> 새해니까 가볍게 손 풀기😄

### `2884`

##### 1. 한 단위로 바꾸기

```python
total_minute = hour * 60 + minute # 분 단위로 바꿈
```

##### 2. 구하고 싶은 시간 = 입력 받은 시간 - 45분

```python
total_minute -= 45 # 원하는 시간 = total_minute - 45
```

##### 3. 다시 시간 단위 바꾸기

```python
result_hour = total_minute // 60 % 24 # 원하는 hour = 전체 시간을 60으로 나눈 몫 mod 24
result_minute = total_minute % 60 # 원하는 hour = (전체 시간) mod 60
```

---

## 01월 02일

> 백트래킹은 왤케 어려운걸까.. 아무리 풀어도 어렵네😂

### `15652`

##### 1. 반복문 돌면서 재귀 호출하기

```python
for i in range(start, N + 1):
    stack.append(i)
    solution(i)
    stack.pop()
```

- `stack.append(i)`: `stack`에 `i` `push`
  - 예시: `[1]` ➜ `[1, 1]`
- `stack.pop()`: 앞에서 넣어준 `i` `pop`
  - 예시: `[1, 1]` ➜ `[1]`

##### 2. 조건 만족하면 출력하고 종료

```python
if len(stack) == M:
    print(*stack)
    return
```

---

## 01월 03일

> 백트래킹 연습(2) - 조합, 순열
>
> ##### 어제 풀었던 문제랑 풀이 비슷

### `15654`

##### ➕ 조건식

```python
if args[i] not in stack
```

- 문제 조건: `(중복 ✖️)`
  - `stack`에 `args[i]`가 없어야 `push`할 수 있음

##### ➕ 반복문 범위

```python
for i in range(n)
```

- `순열`이기 때문에 무조건 `0` ~ `n - 1`까지 다 돌아야됨

### `6603`

##### ➕ 조건식

```python
if args[i] not in stack
```

- 문제 조건: `(중복 ✖️)`
  - `stack`에 `args[i]`가 없어야 `push`할 수 있음

##### ➕ 반복문 범위

```python
for i in range(start, k)
```

- `조합`이기 때문에 무조건 `앞에서 탐색한 부분` 이후부터 돌아야 함
