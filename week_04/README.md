1 # 4주차

> - 완전탐색
> - 힙
> - 깊이 우선 탐색, 넓이 우선 탐색

---

## 21.07.26

> - [2331 - 분해합](https://www.acmicpc.net/problem/2331)
> - [2309 - 일곱 난쟁이](https://www.acmicpc.net/problem/2309)

#####완전탐색 - `무식한 힘`

> brute force : 무식한 힘으로 해결 가능. 😭

_실행 시간이 어마무시하게 많이 걸린다._

`<2331>`

1부터 N까지 탐색하는데

```python
if sum(list(map(int, str(i)))) + i == N
```

다음을 만족하면 그 때의 i를 출력해주고 끝낸다.

`<2309>`

`input`은 9개고 난쟁이의 수는 `7`로 정해져 있다.
`이중 for문`을 돌면서 `난쟁이가 아닌 2명`을 고르면 된다.

---

## 21.07.27

> - [2583 - 영역구하기](https://www.acmicpc.net/problem/2583)
> - [2667 - 단지번호붙이기](https://www.acmicpc.net/problem/2667)
> - [4963 - 섬의개수](https://www.acmicpc.net/problem/4963)

`<2583>`

m x n 행렬을 미리 1로 초기화 시켜놓고 시작

```python
graph = [[1] * n for _ in range(m)]
```

영역을 구해준다.

```python
points = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(points[1], points[3]):
    for j in range(points[0], points[2]):
        graph[i][j] = 0
```

이후에는 1인 구역 개수를 세어주면 된다.!

```python
def dfs(x, y):
    global point_count
    point_count += 1 # 영역안에 있는 점 개수 구하기
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    graph[x][y] = 0
    for cx, cy in zip(dx, dy):
        nx = cx + x
        ny = cy + y
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 1:
            dfs(nx, ny)

point_count = 0
result = []
for x in range(m):
    for y in range(n):
        if graph[x][y] == 1:
            dfs(x, y)
            result.append(point_count)
            point_count = 0
```

`<2667>`, `<4963>`

위의 문제에서 1인 영역 개수를 구해준것 처럼 똑같이 진행하면 된다.

## 🥳

`<11724>`

인접 리스트로 그래프 간선들을 정리해서 사용하였다. `O(N + E)`

1. `먼저 visited list를 n + 1개의 False로 초기화 해주고`
2. `인접 리스트들을 돌면서 방문하지 않은 곳을 True로 바꿔준다.`

그리고 연결 요소 개수를 세어주면 끝!

```python
def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1
```

---
