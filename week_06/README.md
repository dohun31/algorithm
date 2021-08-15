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

## 21.08.08

> - 올리브영 코테 1번
> - [거리두기 확인하기](https://programmers.co.kr/learn/courses/30/lessons/81302)

⏱: 1시간 30분 😭

#### `거리두기 확인하기`

처음 시도했을때 완벽하게 맞췄을거라고 생각했는데 테스트 케이스에서 우루루루 틀렸다.
놓치고 있던 부분 확인

> bfs로 <맨해튼 거리>가 아니라 <거리>를 계산하고 있었음
> 반례) [P X P][o o o] 이 경우에 파티션있어서 안봐도 되는데 꾸역 꾸역 옆에 P까지 가버림. (밑에 길이 있어서)

거리계산에서 맨해튼 거리 계산으로 변경

```python
mh = abs(x - nx) + abs(y - ny) # 파티션이 아니면 맨해튼 거리 계산
    mh_checked[nx][ny], visited[nx][ny] =  mh, True # 맨해튼 거리 갱신, 나 들렸어요
```

그리고 맨해튼 거리가 2이상일떄는 아예 쳐다도 안봄 -> `그 이상은 거리두기 무조건 지킨거임(지금 P 기준)`

그런데 13번 케이스가 계속 통과가 안돼서 맨해튼 거리 체크하던 배열 확인해보니까 2위로는 아예 쳐다도 안볼랬더니 3도 살짝 쳐다봤음..

### `👇👇 문제의 조건`

```python
if mh <= 2: # 맨해튼 거리 1이하일때만 q에 넣음 -> 큐에서 꺼낼때 + 1 되니까 결국엔 거리가 2인애들까지임
    q.append((nx, ny))
```

> 큐에 2까지 넣어버리면 다음 반복문에서 걔 다음 맨해튼 거리까지 측정함(3)
> 따라서 1까지만 넣으면 2까지하고 끝냄.

### `👇👇 수정 조건`

```python
if mh <= 1: # 맨해튼 거리 1이하일때만 q에 넣음 -> 큐에서 꺼낼때 + 1 되니까 결국엔 거리가 2인애들까지임
    q.append((nx, ny))
```

### `쉬운척 하면서 어렵고, 어려운척 하면서 막상 까보면 쉬운..?`

`<올리브영 코테 1번>`

1. `모든 원을 다 포함하는 최소의 직사각형 찾기`

```js
let min = (a, b) => {
  return a > b ? b : a;
};

let max = (a, b) => {
  return a > b ? a : b;
};

let [l, b, R, t] = [201, 201, 0, 0]; // 반지름 0 ~ 100임
for (let i = 0; i < x.length; i++) {
  l = min(l, x[i] - r[i]);
  b = min(b, y[i] - r[i]);
  R = max(R, x[i] + r[i]);
  t = max(t, y[i] + r[i]);
}
```

2. `난수로 x, y 좌표 만들기`

```js
let points = [];
for (let i = 0; i < v.length; i += 2) {
  points.push([l + (v[i] % (R - l)), b + (v[i + 1] % (t - b))]);
}
```

3. `만든 점들 중에서 원 안에 있는 점들만 살리기`

```js
function check(a, b, x, y, v) {
  let flag = false;
  for (let i = 0; i < x.length; i++) {
    // 현재 원의 중심이랑 점이랑 거리가 현재 원의 반지름보다 크거나 작다면 원 안에 있는 점.
    if (Math.sqrt(Math.pow(x[i] - a, 2) + Math.pow(y[i] - b, 2)) <= r[i]) {
      flag = true;
    }
  }
  return flag;
}

result_points = points.filter((point) => {
  return check(point[0], point[1], x, y, r);
});
```

4. `최종 결과 return하기`

```js
return Number((result_points.length / points.length) * (R - l) * (t - b));
```

---

# 6주차 소감

> 그래프 재밌다.. 너무 재밌다..
> 오늘 올리브영 코테 쳐봤는데 실전 연습을 많이 해야겠다. 외부 ide안쓰는 연습이랑 코드 힌트 없이 코딩하기 등등
> 아 그리고 js 연습도 자주 해야할듯.
> 나중에 프론트엔드 코테칠때 js로 많이 치는데 오늘 js로 해보니까 어질어질 하네.

---
