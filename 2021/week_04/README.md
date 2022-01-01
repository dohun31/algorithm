1 # 4주차

> - 완전탐색
> - 힙
> - 깊이 우선 탐색, 넓이 우선 탐색

---

## 21.07.26

> - [2331 - 분해합](https://www.acmicpc.net/problem/2331)
> - [2309 - 일곱 난쟁이](https://www.acmicpc.net/problem/2309)

##### 완전탐색 - `무식한 힘`

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

## 21.07.28

> - [2178 - 미로 탐색](https://www.acmicpc.net/problem/2178)
> - [2468 - 안전 영역](https://www.acmicpc.net/problem/2468)

`<2178>`

`bfs`는 항상 감이 안잡혔는데 구글링하면서 한번 풀어보니까 감이 잡혔다. 🤩

`<2468>`

처음 문제는 어제 봤는데 얼핏 보고

> 아 n이 주어지고 그 이하인거만 세면 되는거구나

라고 생각했는데 그냥 2차원 배열에 있는 모든 숫자들을 n으로 두고 그 중에 최대값을 찾는거여서 극혐이어서 도망쳤다.

근데 계속 머리에 생각이나서 이리저리 생각해보니까 별로 어려운것은 아니었다.

1. `2차원 배열 입력받을때 중복없이 수들을 기록하기`
2. `차례대로 n으로 두고 n 이상인 지역들의 덩어리 개수만 구해주면 된다.`

이 과정에서 어려움이 하나 있었는데 `배열 복사`였다.
여러번 탐색을해야해서 다른 변수를 두고 `graph`를 매번 복사해서 사용하려고 했는데 `모든 행이 똑같거나`, `앞의 결과가 유지`되는 상황이 계속 벌어졌다.

알고보니 나는 계속 `얕은 복사`를 하고 있었다.

그래서 graph를 복사해서 `return`해주는 함수를 만들어서 사용하였다.

```python
def new_graph():
    _graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            _graph[i][j] = graph[i][j]
    return _graph
```

- 문제보고 겁먹지 말기👊🏻

---

## 21.07.29

> - [1012- 유기농 배추](https://www.acmicpc.net/problem/1012)
> - [7576 - 토마토](https://www.acmicpc.net/problem/7576)
> - [10026 - 적록색약](https://www.acmicpc.net/problem/10026)
> - [14502 - 토마토](https://www.acmicpc.net/problem/14502)

`<1012>`

이 문제는 앞서 계속 했던 덩어리 찾기(?)문제이다.

근데 중간에 점들을 위치를 받을 때 변수이름을 잘못 정해서 중복 선언이 되었다.(변수 선언할때 주의하기)

매번 덩어리 찾기 문제는 `dfs`로만 풀어봤었는데 `bfs`연습할겸 풀어봤다.

`<7576>`

`1인 지점`에서 점점 영역을 넓혀가다가 더이상 못하게되면 중단한다.

탐색이 끝났는데 `0인 지점`이 있다면 -1을 출력해야한다.
0을 조금 더 쿨하게 찾을 수 있을 것 같은데 하는 미련이 계속 남는다.
구글링을 하다가 내 코드보다 쿨한 코드 발견!

```python
for g in graph:
    if 0 in g:
        flag = False
```

`in`의 존재를 잊고 있었다... 반성 또 반성 다음에는 바로 생각이 나길

`<10026>`

그냥 dfs한 번, 적록색약 dfs한 번 돌리려고 했는데 그건 너무 파이썬답지 않아서 머리를 엄청 굴려서 해결해보았다.

1. `적록색약이 보는 graph를 따로 구현한다.`

```python
n_graph = copy.deepcopy(graph)
for i in range(n):
    for j in range(n):
        if n_graph[i][j] == 'G':
            n_graph[i][j] = 'R'
```

2. `graph와, color를 원본이랑, 적록색약본이랑 2개를 준비한다.`

```python
graphs = [graph, n_graph]
colors = [['R', 'G', 'B'], ['R', 'B']]
```

3. `그러면 똑같은 반복문으로 처리가 가능하다.😁`

```python
for color, gp in zip(colors, graphs):
    count = 0
     _graph = copy.deepcopy(gp)
    _visited = copy.deepcopy(visited)
    for c in color:
        for i in range(n):
            for j in range(n):
                if _graph[i][j] == c and not _visited[i][j]:
                    dfs(i, j, c)
                    count += 1

    print(count, end=' ')
```

`<14502>`

모든 경우를 다 돌아봐야하는 `브루투포스` 문제이다. 거기다 이제 `bfs`를 곁들인..

모든 경우는 `combination`을 사용해서 구했다.

이 경우들만 구했다면 그 뒤부턴 단순 탐색 문제이다.

---

## 21.07.30

> - [1417 - 국회의원 선거](https://www.acmicpc.net/problem/1417)
> - [18511 - 큰 수 구성하기](https://www.acmicpc.net/problem/1417)

`<1417>`

다솜이는 다른 모든 후보들보다 큰 표를 가져야 한다. 그러기위해 필요한 최소의 표가 몇장인지 구해야 한다.

1. `다솜이를 제외한 사람들의 표를 내림차순으로 정렬한다.`

```python
other.sort(reverse=True)
```

2. `제일 큰 사람이(other의 제일 첫번째 사람)이 다솜이 보다 작기 전까지 한표씩 가져온다.`

```python
while dasom <= other[0]:
    other[0] -= 1 # 제일 큰 사람 한 표를 뺏음.
    dasom += 1 # 다솜이 표를 하나 추가
    count += 1 # 매수한 표가 몇 표인지 세어줌
    other.sort(resverse=True) # 다시 내림차순으로 정렬
```

`<18511>`

어제 조합으로 풀었던 문제랑 비슷해보여서 바로 조합 사용! 그런데 중복을 곁들인..

> 입력값으로 받은 `set`중에서 중복으로 n의 길이만큼 뽑고, 뽑은 숫자문자들을 합쳐서 숫자로 만들어주고, n이랑 비교하면서 max값을 구함!

> - #### ⚠️ `꼭 n이랑 같은 길이가 아닐 수도 있다.`
>   > 예를 들어 22 3 7 8 이라면 22보다 작은 최대의 값이 8이 된다.
>
> * #### `따라서 len(n)과 len(n-1)을 다 구해봐야한다.`
>   > len(n)에 최대의 값이 안나온다면 무조건 len(n-1)에 나옴. len(n-k) (k>1)은 볼 필요 없음!

---

## 21.07.31

> - [1436 - 영화감독 숀](https://www.acmicpc.net/problem/1436)
> - [2206 - 벽 부수고 이동하기](https://www.acmicpc.net/problem/2206)
> - [22352 - 항체 인식](https://www.acmicpc.net/problem/22352)

`<1436>`

`브루투포스` 문제

영화감독이 좋아하는 최소의 값은 666이므로 666부터 세어주면 된다.

```python
if '666' in str(number): # 만약에 숫자에 666 세개 이상 포함돼있으면
    count += 1 # 하나 세어 줌
```

> _처음에 if str(number) in '666'이라고 했다가 무한 루프를 돌았던...😂_

`<2206>`

나름 자신있게 풀었는데 반례가 너무 많았던 문제...

벽이 있는곳을 따로 저장해놨다가 `for`문을 돌면서 벽을 부수고 가는 식으로 했는데

> 벽을 안부서도 최소값이 나올 수 있다.

위의 조건을 생각을 못했다.

- #### 결국 구글의 힘을 빌렸다.
  > 처음보는 3차원 배열이 나왔다.
  > graph[x][y][0], graph[x][y][1]을 두고, 3번째 인덱스가 0이면 벽을 안부순경우, 1인경우는 벽을 부순경우이다.

### `더 열심히 공부해야겠다.`

`<22352>`

문제는 어렵게 보이는데 막상 보면 똑같은 `덩어리찾기`문제이다.

1. `하나씩 보다가 백신 맞기 전의 위치의 값과, 맞은 후의 위치의 값이 다르다면 주변 탐색을 시작한다.`

```python
for i in range(row):
    for j in range(col):
        if count > 1: # 덩어리 개수가 1을 넘어가면 원하는 백신이 아님
            print('NO')
            quit()
        if nv_graph[i][j] != v_graph[i][j] and not visited[i][j]:
            dfs(i, j)
            count += 1
```

2. `상하좌우 탐색할 때 조건을 만족하면 계속 탐색한다.`
3. `조건을 만족하지 않으면 탐색 중지`

```python
 if 0 <= nx < row and 0 <= ny < col:
    if nv_graph[nx][ny] == nv_graph[x][y] and not visited[nx][ny]:
        if v_graph[nx][ny] != v_graph[x][y]:
            print('NO')
            quit()
        dfs(nx, ny)
```

---

## 21.08.01

> - [1743 - 음식물 피하기](https://www.acmicpc.net/problem/1436)

#### `1743 - 음식물 피하기`

⏱: 20분

매번 풀었던 `덩어리문제`
쉽게 풀었다.

---

# 4주차 소감

> 처음에는 dfs, bfs 너무 어려워했는데 첫날 해보고 나니까 그냥 거의 문제들이 비슷해보였다. 매번 말하는 `덩어리 찾기`
> 많이 찾아보니까 이제 쉬워졌다.
> 그런데 아직 힙은 조금 어렵다.. 솔직히 힙 어려워서 진짜 조금 풀었는데 마지막 주에 힙 많이 풀어서 연습해야겠다..

> 아 그리고 어제 ucpc2021 대회하길래 슬쩍 문제 풀었는데 파이썬 유저사이에서 실행시간 제일 짧게 나와서 나름 뿌듯 ㅎㅎ 그런데 파이썬으로 메모리 관리하는법을 공부해야겠다. 메모리 너무 많이 쓴다..
