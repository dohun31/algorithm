# 9주차

---

## 21.09.02

> - [9466 - 텀 프로젝트](https://www.acmicpc.net/problem/9466)

차근차근 읽어보니까 결국엔 `사이클`을 찾는 문제였다.

1. `방문하지 않은 노드라면 dfs()해주기`

```python
for idx, num in enumerate(graph):
    if not visited[idx]:
        stack = []
        dfs(idx)
```

> `stack: 지금까지 지나간 노드를 기억하기`

2. `def dfs()`

> 2-1. `방문한 노드 stack에 push, 방문 처리`

```python
stack.append(idx)
visited[idx] = True
```

> 2-2. `현재 노드가 가리키는 노드 탐색`

```python
    next_idx = graph[idx] # 현재 정점이 가리키는 정점
    if visited[next_idx]:
        if next_idx in stack:
            global cnt
            cnt += len(stack[stack.index(next_idx):])
        return
    else:
        dfs(next_idx)
```

원래 짰던 코드는 계속 80퍼에서 시간초과가 났다.

#### 👇👇 원래코드

```python
def dfs(idx):
    stack.append(idx)
    visited[idx] = True # 일단 방문함

    next_idx = graph[idx] # 현재 정점이 가리키는 정점
    if next_idx in stack: # 가리키는 정점이 stack안에 있다면 -> 사이클
        global cnt
        cnt += len(stack[stack.index(next_idx):])
    else:
        if not visited[next_idx]: # 같지않고 방문하지 않은 정점이라면
            dfs(next_idx)
```

#### 👇👇 시간초과 이유

`아마 이 놈 때문인것 같다.`

```python
if next_idx in stack:
```

매번 탐색할때마다 next_idx가 stack에 있는지 확인하면 저 조건문의 최악의 시간 복잡도는`O(len(stack))`가 된다. ㅁㅊ..

#### 👇👇 고친 코드

```python
if visited[next_idx]:
    if next_idx in stack:
```

다음에 가야하는 노드가 이미 방문한 노드라면 if문을 실행한다.

---
