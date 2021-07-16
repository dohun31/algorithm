# 2주차

> - stack
> - queue
> - list

---

## 21.07.12 - stack

> - [4949 - 균형잡힌 세상](https://www.acmicpc.net/problem/4949)
> - [2504 - 괄호의 값](https://www.acmicpc.net/problem/2504)

<4949>

여는 괄호가 나오면 stack에 insert하고,
닫는 괄호가 나오면 쌍이 있는지 확인만 해주면 되는 문제여서 쉽게 풀었음

제출하는데 틀렸다고해서 봤더니 yes or no로 출력해야 하는걸 YES of NO로 출력해놔서 다시 고쳐서 제출하니까 맞음

<2504>

1. sum과 누적값 변수를 만들어서 0으로 초기화함.  
   stack이 비었을 때 누적값 > 0 이라면 sum += 누적값 \* (2 or 3), 누적값 = 0.  
   stack이 비었을 떄 누적값 == 0 이라면 sum += (2 or 3).  
   stack이 안비었을 떄 누적값 += (2 or 3)

이렇게 할 경우에 (()[[]])와 같이 () + [[]] 의 경우는 계산 오류가 남.

2. 여는 괄호일 때 sum[-1]이 0이 아니라면 sum에 0을 push해 줌.  
   괄호 한 쌍이 나오고.  
   sum[-1]이 0이면 sum[-1] += (2 or 3).  
   sum[-1]이 !0이면 sum[-1] \*= (2 or 3).

이렇게 할 경우에 더 복잡해짐

3. 닫는 괄호일때 stack[-1]이 정수라면 싹다 더하고 한쌍 만들어지면 \*(2 or 3)하고 push.  
   ex) (()) -> ['(', 2] 인 상태에서 )가 들어오면 stack[-1]이 정수이므로 2 \* 2 가 stack에 남게됨.  
   따라서 마지막에 stack에 정수들만 남는다면 모두 더한 값을 출력, 아니라면 0 출력.

생각보다 시간이 오래걸렸음

---

## 21.07.13 - stack

> - [5397 - 키로거](https://www.acmicpc.net/problem/5397)
> - [1918 - 후위표기식](https://www.acmicpc.net/problem/1918)
> - [17298 - 오큰수](https://www.acmicpc.net/problem/17298)

<5397>

처음에 문제보고 list.insert(index, value), pop(index) 이용해서 풀었는데 시간 복잡도가 너무 커져서 계속 시간 초과.
그래서 슬라이싱 이용해서 풀었는데도 계속 시간 초과…

그래서 구글링 해서 찾은 방법

- left stack, right_stack을 두고 왔다갔다 -> 신선한 충격…

문제보면 조금 더 생각해보기

<1918>

이 문제는 다 풀어 놓고 출력을 이상하게 해서 계속 틀렸음
join으로 출력을 했었는데 그냥 마음 편하게 while문 돌면서 pop하니까 해결... 허무해라

<17298>

어떻게 풀지는 다 생각했는데 그걸 구현을 못한 그런... 구글링하니까 방법은 똑같은데 되게 코드를 잘 짜셨길래 보고 다시 풀었다

---

## 21.07.14 - queue

> - [1158 - 요세푸스 문제](https://www.acmicpc.net/problem/5397)
> - [2161 - 카드1](https://www.acmicpc.net/problem/2161)

<1158>

5분정도 고민해보니까 큐로 어떻게 풀지 생각이 나서 바로 시작.

1. 일단 큐에 1 ~ N 까지 다 push함
2. 변수 i를 두고 k개를 계속 체크
3. while 문에서 큐가 빌 때 까지 i를 증가시키면서 pop한다. 이떄 i == K일 떄만 pop하고 i는 다시 1로 초기화함

풀다가 잠시 막힌 부분이 있었는데

- N이 K보다 작을때

  > - 처음에는 queue의 크기가 k보다 작으면 그냥 순서대로 pop하라고 했는데 생각해보니까 반례들이 너무 많았다. -> 첫 시도에서 틀림
  > - 그래서 시간이 너무 오래걸리지 않을까? 고민은 했지만 방법이 딱히 기억이 안나서 그냥 while문으로 계속 돌렸다. -> 역시나 시간 초과
  > - 고민하다가 pypy3로 제출하니까 시간안에 성공! pypy3.. 감사 ~

- 출력
  > - 출력을 <1, 2, 3> 형태로 요구해서 아래 처럼 하려고 했는데 숫자 사이에 ', '도 있고 마지막 숫자는 또 공백이 없고 좀 까다로웠음.
  ```python
  print('<')
  # pop한 값들을 result에 담아놨음
  while result:
     print(result.pop())
  print('>')
  ```
  > - 그래서 내가 좋아하는 join을 쓰기로 함
  ```python
  print('<' + ', '.join(result) + '>')
  ```

<2161>

문제를 읽어봤더니 그냥 간단한 구현 문제여서 쉽게 풀었음

---

## 21.07.15 - queue

> - [1966 - 프린터 큐](https://www.acmicpc.net/problem/1966)

<1966>

시간제한 2초를 보고 마음을 놨다. 요즘 제일 신경쓰는게 시간제한...

queue를 하나 두고 입력된 정보를 담는다.
이 때 queue에 [data, index]형태로 담음

입력된 정보도 sort해 둔다.

1. queue에서 한 개 pop함.
2. index가 target이랑 같고 data가 max값이라면 result출력
3. index가 target이랑 같지 않을 때, data가 max값이라면 max값을 pop함. 아니라면 다시 queue에 push함.

한 번에 성공!
그런데 더 효율적인 코드가 있어서 구글링하면서 공부중.
그리고 듣고 싶었던 강의 결제해서 오늘은 한개만 풀었다~~!

---

## 21.07.16 - list, queue

> - [1406 - 에디터](https://www.acmicpc.net/problem/1406)
> - [기능 개발](https://programmers.co.kr/learn/courses/30/lessons/42586)

<1406>

7월 13일에 풀었던 키로거 문제랑 비슷한 유형이어서 바로 그떄 봤던 멋진 풀이 적용했다~~
진짜 cool한 코드..

그리고 원래라면 이렇게 썼는데

```python
if left_list:
   right_list.append(left_list.pop())
```

if 말고도 and or 연산자 잘 쓰고 싶어서

```python
left_list and right_list.append(left_list.pop())
```

and연산자 사용해서 코드를 짰다.

<기능 개발>

앞선 기능이 완성되어야 뒤의 기능도 배포를 할 수 있다
그래서 현재 진도와, 진행 속도로 배포까지 며칠 걸리는지 계산해서 큐에 차례대로 push했다.
이 때 며칠 걸리는지 계산은 아래와 같이 계산했다.

```python
import math
day = math.ceil((100 - progress) / speed)
```

day = [7, 3, 9]라면 큐를 사용해서 먼저 7을 pop하고 7보다 큰 숫자가 나올 때 까지 pop하고 개수를 count한다. 이런식으로 큐가 빌 때까지 반복하면 답이 나온다.

처음 시도에서 테스트 케이스 몇 개가 틀려서 황당했는데 알고봤더니 여기가 문제였다..!!

```python
if now_data > queue[0]:
   result[-1] += 1
   queue.popleft()
```

배포까지 걸리는 날이 같을 경우에 대해서 생각을 못했다.
한 글자 더 추가하니까 성공~~

```python
if now_data >= queue[0]:
   result[-1] += 1
   queue.popleft()
```

---
