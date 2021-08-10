# 6주차

> - 그래프

---

## 21.08.09

> - [5567 - 결혼식](https://www.acmicpc.net/problem/5567)
> - [6118 - 숨바꼭질](https://www.acmicpc.net/problem/6618)

`<5567>`

친구관계는 양방향 이므로 `양방향 그래프`를 사용하면 된다.

`내 친구`들을 먼저 조사 하고 `내 친구의 친구`를 조사하면 끝!

`<6118>`

`bfs`로 구현해서 테스트 케이스는 분명히 통과했는데 제출하니까 시간 초과..
pypy3로 했는데 메모리 초과..
정말 진퇴양난이네..

---

## 21.08.10

> - [1753 - 최단경로](https://www.acmicpc.net/problem/1753)
> - [1916 - 최소비용 구하기](https://www.acmicpc.net/problem/1916)
> - [6118 - 숨바꼭질](https://www.acmicpc.net/problem/6118)
> - [11403 - 경로찾기](https://www.acmicpc.net/problem/11403)
> - [11404 - 플로이드](https://www.acmicpc.net/problem/11404)
> - [18352 - 특정 거리의 도시 찾기](https://www.acmicpc.net/problem/18352)

`<1753>`

다익스트라 연습할 겸 동빈나 강의 들으면서 했다.

##### 1. `힙(우선 순위 큐)`를 사용하면 더 효율적인 코드를 짤 수 있다.

##### 2. `갱신`될 때만 힙에 push

`<1916>`

그냥 평범한 다익스트라 문제인데 틀렸습니다가 떠서 잠시 고민하다가 문제의 코드를 찾았다.

```python
INF = int(1e6)
```

ㅋㅋㅋㅋ....

```python
INF = int(1e9)
```

로 변경하니까 바로 정답!

`<6118>`

어제 `bfs`로 실패했던 문젠데 `다익스트라로` 다시 풀어봤다.

매 단계에서 비용은 다음과 같이 측정했다. (가중치가 따로 없음, 비용 -> 순수 거리)

```python
cost = dist + 1
```

출력값은 아래처럼 접근 가능하다.

```python
max_dist = max(distance[1:]) # 숨을 수 있는 제일 먼 거리
max_dist_idx = distance.index(max_dist) # 먼 거리 중에 번호가 제일 작은 노드
max_dist_cnt = distance.count(max_dist) # 먼 거리의 노드 개수
print(max_dist_idx, max_dist, max_dist_cnt)
```

`<11403>`

`플루이드 와샬`알고리즘을 사용하면 쉽게 해결 가능하다.

##### `i -> k -> j`로의 길이 있다면 `i -> j`길이 있다고 할 수 있다.

```python
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] + graph[k][j] > 1:
                graph[i][j] = 1
```

`<11404>`

단순 `플루이드 와샬`문제인데 코드 한줄을 못써서 계속 틀렸다.

조건 `시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.`을 놓쳐서..
인접 행렬 정보를 입력받을때 다음 코드를 추가하면 된다.

```python
graph[a][b] = min(c, graph[a][b])
```

`<18352>`

다익스트라 알고리즘을 사용해서 x에서의 최단거리를 찾은 뒤 출력할때 간단한 조건만 넣으면 된다.

```python
if k in distance:
    for idx, dist in enumerate(distance):
        if dist == k:
            print(idx)
else:
    print(-1)
```

---
