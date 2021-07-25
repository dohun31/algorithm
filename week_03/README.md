# 3주차

> - string
> - hash
> - sort

---

## 21.07.19

> - [1269 - 대칭 차집합](https://www.acmicpc.net/problem/1269)
> - [1316 - 그룹 단어 체커](https://www.acmicpc.net/problem/1316)
> - [1541 - 잃어버린 괄호](https://www.acmicpc.net/problem/1541)
> - [1544 - 사이클 단어](https://www.acmicpc.net/problem/1544)
> - [1764 - 듣보잡](https://www.acmicpc.net/problem/1764)
> - [2577 - 숫자의 개수](https://www.acmicpc.net/problem/2577)
> - [2751 - 수 정렬하기2](https://www.acmicpc.net/problem/2751)

`<1269>`

저번에 프로그래머스 풀 때 counter모듈 썻던 기억이 있어서 바로 이용해봤다.

```python
A = Counter([1, 2, 3, 4, 5])
print(A)
#{1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
```

counter를 이용하면 이렇게 된다.

차집합도 쉽게 구해진다 ~.

`<1316>`

이 문제는 dict 자료형을 사용했다. 사실 투머치같다고 생각이 드는데 그냥 보자마자 든 생각이 dict이어서 일단 실행에 옮겼다.

1. `처음 나오는 알파벳이면 {'알파벳' : True}를 추가해준다.`
2. `만약에 알파벳이 이전에 나온 알파벳이고 앞의 알파벳이랑 같다면?(연속된다면) 통과`
3. `그런데 이전에 나온 알파벳인데 앞의 알파벳과 연속되지 않는다면? flag를 false로 바꿔주고 뒤를 더 볼 필요가 없으므로 break해준다.`
4. `flag가 true라면 count를 세주고`
5. `count 출력`

`<1541>`

처음 봤을때 실버 2 문제라길래 겁먹었는데 잠시 생각해보니까 너무 간단한 문제였다.

\- 가 나온 이후론 모든 숫자를 - 붙여서 더해주면 된다.
ex) 55 - 20 + 30 - 39 + 30
=> 55 - (20 + 30) - (39 + 30)
=> 55 - 20 -30 -39 -30
이렇게 처음 - 이후의 숫자들은 모두 음수로 바꿔지고, 결국은 제일 최소의 결과가 된다.

`<1544>`

이번에도 dict 자료형을 사용했다
사이클 문자열인지 보려면 입력받은 문자열을 두번 합쳐서 검사하면 된다.

ex) dict: {'elloh': 1}라고 치고
입력값이 "hello" -> hellohello이고 이때 elloh가 hellohello안에 있는지 검사해주면 된다.

```python
if len(key) == len(data) and (key in data * 2):
```

시간을 조금이라도 줄이려면 입력값과 key의 길이가 같을때 만 비교해주면 된다.!

`<1764>`

여기서도 counter를 활용했다

우선 듣지도 못한 친구들과 보지도 못한 친구들을 counter 모듈로 만들어 주고
둘을 합쳤다..!

듣지도 보지도 못한 친구라면 이름이 2번이나 언급된다. 따라서 조건에 맞는 이름을 정렬해서 출력해주면 된다.

`<2577>`

그냥 문제에서 하라는 대로 하면 성공 !

`<2751>`

그냥 당차게 풀었다가 메모리를 다 써버려서 틀렸다. 그래서 문제에서 10000개 이하의 숫자가 주어진다 해서 그냥 카운터 정렬로 풀었다.
카운터 정렬은 실전에서 처음 써보는데 일정 범위 숫자만 있다면 쓸 수 있겠는데 범위가 너무 넓다면 굳이 안쓰고 싶은? 그런 정렬

---

## 21.07.20

> - [2941 - 크로아티아 알파벳](https://www.acmicpc.net/problem/2941)
> - [5052 - 전화번호 목록](https://www.acmicpc.net/problem/5052)
> - [5430 - AC](https://www.acmicpc.net/problem/1541)
> - [9935 - 문자열 폭발](https://www.acmicpc.net/problem/1544)
> - [10816 - 숫자카드2](https://www.acmicpc.net/problem/10816)
> - [11656 - 접미사 배열](https://www.acmicpc.net/problem/2577)
> - [숫자문자열과 영단어](https://programmers.co.kr/learn/courses/30/lessons/81301)

`<2941>`

크로아티아 알파벳이 몇개 없어서 배열에 미리 넣어주고 replace를 사용했다.

조금 실수했던 부분은 nljj 에서 lj를 먼저 지우고 nj가 됐을 때 다시 nj도 지워버려서 replace문을 수정했다
(전)

```python
data = data.replace(c_data, '')
```

(후)

```python
data = data.replace(c_data, ' ')
```

이후에 공백은 빼주었다.

`<5052>`

처음 문제 이해가 조금 어려웠다.
제일 먼저 긴급번호가 주어지고 그 뒤에 서로 비교하는줄 알고 문제를 풀었는데 그냥 서로서로 다 비교하는거였다.

sort하게 되면 겹칠수 있는 `가능성이 있는 애들이 붙어있게 된다`. 따라서 i번째와 i + 1번쨰를 서로 비교해주면 된다.

`<5430>`

예제는 맞췄는데 시간 초과가 떴다..
reverse를 진짜 `reverse안하는 방법`을 생각해봤다.

1. `RR이 나오면 없애줌`
2. `R일때 left를 not 해줌`
3. `D일떄 left가 true면 reverse 안된거니까 popleft()`
4. `D일때 left가 false면 reverse 이니까 pop()`
5. `출력전 left가 false라면 reverse해주고 아니면 그대로 출력`

`<9935>`

처음부터 폭탄인지 확인하는거보다 마지막글자가 똑같을때 앞을 살펴보는것이 적절하다.
왜냐하면 폭탄이 c4일때 문자열이 ccc4라면 c가 나올때마다 뒤가 4인지 검사해줘야 한다.
따라서 4가 나올떄만 앞이 c인지 확인해주면 된다.

```python
if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
            if ''.join(stack[-len(bomb):]) == bomb:
                for _ in range(len(bomb)):
                    stack.pop()
```

`<10816>`

간단한 dict 자료형을 사용하는 문제이다.
데이터들이 주어지면 dict에 넣어주고 count해준다.
그리고 개수를 물어보면 디폴트값을 0으로 해주고 답해주면 된다.

```python
result.append(dict.get(i, 0)) # dict에 key == i 가 있으면 value를 반환하고,
# 아니라면 설정해준 default값(0)을 반환.
```

`<11656>`

파이썬 너무 좋다...줄줄줄 적으면서 이게 되나? 싶은데 `이게 된다..!`

```python
print('\n'.join(sorted([data[i:] for i in range(len(data)))))
```

`<숫자문자열과 영단어>`

크로아티아 알파벳이랑 비슷한 문잔데 0~9개만 미리 영어로 바꿔놓기만 하면 금방 풀리는 문제이다.

```python
for i in range(len(numbers)):
        # 문자 숫자를 포함하고 있으면 replace해줌.
        s = s.replace(numbers[i], str(i))
```

---

## 21.07.21

> - [1181 - 단어정렬](https://www.acmicpc.net/problem/2941)
> - [11650 - 좌표정렬하기](https://www.acmicpc.net/problem/11650)

`<1181>`

`조건`

1. `길이가 짧은 것부터`
2. `길이가 같다면 사전 순으로`

정렬에 조건을 사용하려면 다음과 같이 하면 된다.

```python
sorted(list, key = lambda x: (condition1, condition2))
```

이때 `condition`에 `+`, `-`를 붙이면 `오름차순`, `내림차순`으로 바꿀 수 있다.

`<11650>`

앞 문제에서 사용했던 `key`를 사용한다면 쉽게 풀리는 문제.
그런데 '틀렸습니다'가 떴다...
다시 보니까 좌표들을 문자 상태로 sort 했던 것이다.

그래서 다시 int형으로 형변환해주고 다시 sort하니까 성공!

---

## 21.07.22

> - [1744 - 수 묶기](https://www.acmicpc.net/problem/1744)
> - [10814 - 나이순 정렬](https://www.acmicpc.net/problem/10814)
> - [11651 - 좌표 정렬2](https://www.acmicpc.net/problem/1744)

`<1744>`

오 그냥 내림차순으로 `sort`해서 큰 수부터 2개씩 곱해주면 되겠네? 하고 당차게 풀기 시작.
결과는 `틀렸습니다.`

생각해보니까 내 로직에 문제점이 있었다.

1. `조건문을 "곱했을때 0보다 크거나 같다면 곱해라"라고 설정해서 (양수 * 0), (1 * 양수)같은 case를 처리하지 못했다.`
2. `내림차순으로 sort 하면 음수는 절대값이 작은 수 부터 시작된다.`

먼저 첫번째 문제부터 고쳐보았다.

```python
if number == 1:
    result.append(number)
```

이렇게 하면 양수일 때는 잘 돌아갔지만 음수가 섞이기 시작하면 틀린 답이 나왔다.

그래서 원래 숫자는 보존하면서 절댓값이 큰 순서대로 sort해 주기 위해서 음수와 양수, 그리고 0을 따로 다뤘다.

```python
p_numbers, n_numbers, z_numbers = [], [], []
```

p_numbers는 앞의 로직과 동일하게 진행하였다.

n_numbers일 때는 생각할게 아래와 같다.

1. `음수의 개수가 짝수면 무조건 2개씩 곱한다.`
2. `음수의 개수가 홀수면 무조건 zero가 있을때 0이랑 곱했다 치고 절대값이 작은 음수를 pop한다.`

핵심은 `음수는 곱해서 양수로 만들자`이다.

따라서 `p_numbers에서의 결과`와 `n_numbers`를 합하면 된다.

z_numbers는 아무리 많이 있어도 최대 한 개만 사용된다.
(n_numbers가 홀수일때 절대값 제일 작은 놈 제거 용)

일단 풀었긴 한데 좀 더 clean한 코드가 있을 것 같다. 다시 고쳐야 할 듯..

`<10814>`

`sort`할 때 `key`로 나이를 주면 끝!

`<11651>`

이전에 풀었던 좌표 정렬에서 우선순위가 `y좌표가 큰 순서대로`로 바뀐 것 밖에 없다.

이렇게 날로 먹어도 되나 싶을 정도로 간단..

그대신 내일 어려운거 풀어야지

---

## 21.07.23

> - [1302 - 베스트셀러](https://www.acmicpc.net/problem/1302)
> - [1620 - 나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)
> - [2002 - 추월](https://www.acmicpc.net/problem/2002)
> - [13414 - 수강신청](https://www.acmicpc.net/problem/13414)
> - [17219 - 비밀번호 찾기](https://www.acmicpc.net/problem/17219)

`<1302>`

`Counter`를 사용해야겠다 생각은 했는데 dict를 사용하면 항상 딜레마에 빠지는게 `제일 처음(마지막) 데이터에 어떻게 접근하지?` 이다.

일단 많이 읽은 순서대로 sort하는 것은 성공했다.

제일 처음 값에 접근해야 하는데 처음과 끝, 순서라는 개념이 dict에는 존재하지 않는다.
그러던 중 most_common이라는 Counter 함수를 발견했다.

```python
most_common_books = books.most_common(1)[0][0]
```

> - most_common(1) - counter가 높은 순으로 1개를 뽑음 - [(), (), ...]형태로 주어짐
> - most_common(1)[0] - 0번째 행에 접근
> - most_common(1)[0][0] - 0번째 행의 0번째 열에 접근

`<1620>`

dict형에 들어오는 순서대로 key를 주고, value를 정해주면 쉽게 풀림.

`<2002>`

처음 문제를 볼때는 차선은 몇 줄 인건가? 고민했는데 test case들을 보니까 차선이 1개였다.

해시 문제여서 어떻게 하면 dict로 풀 수 있을까 고민했다. 근데 아무리 생각해도 dict로는 순서에 관여할 수 없을 것 같아서 포기했다.

그래서 순서하면 바로 떠오르는 list로 풀어기로 했다.

먼저 생각한 로직은 다음과 같다.

1. `나온 차가 list의 제일 첫번째 차라면, list[0]를 지워준다.`
2. `아니라면, 추월한 차 대수를 세고, 그 차의 index를 구해서 list에서 그 차를 제거해준다.`

예를 들어 [1, 2, 3, 4, 5]로 차가 들어왔는데 [5, 1, 3, 2, 4]로 나갔다고 하자.

1. `5는 list[0]이 아님 -> list = [1, 2, 3, 4], count = 1`
2. `1은 list[0]이 맞음 -> list = [2, 3, 4], count = 1`
3. `3은 list[0]이 아님 -> list = [2, 4], count = 2`
4. `2는 list[0]이 맞음 -> list = [4], count = 2`
5. `4는 list[0]이 맞음 -> list = [], count 2`

따라서 이 경우에 반드시 추월하였다고 생각할 수 있는 차는 2대이다.

시간을 최대한 적게 쓰고 싶어서 slicing을 하였다.

`<13414>`

클릭을 여러번 하면 제일 최근에 한 클릭으로 인정이 된다. (`우선순위가 밀리게 된다.`)
사람이름이 들어올때마다 순서를 갱신해준다.

처음 시도에 인덱스 에러가 떠서 당황했다.

그런데 알고 보니까 `정원보다 수강신청한 사람이 적을 경우`를 생각하지 못했다.

따라서 출력하기 전에 K를 다시 갱신해 주었다.

```python
if K > len(students):
    K = len(students)
```

`<17219>`

단순 dict 사용 문제여서 쉽게 풀었다.

get함수를 사용할지, key로 바로 접근할지 고민했다.

> - get은 있는지 없는지 확신이 안설때 사용하는 함수라고 생각했다.
> - 그런데 이 경우에는 무조건 있는 value만 검색하기때문에 바로 key에 접근하는 방식을 사용했다.

---

## 21.07.24

> - [18870 - 좌표압축](https://www.acmicpc.net/problem/18870)

`<18870>`

`dict` 자료형과 `list`둘 다 사용해야 하는 문제였다.

1. `중복 제거된 입력값들을 정렬`
2. `정렬된 값을 key는 입력값, value는 순서로 선언`
3. `입력값들을 돌면서 dict[입력값]을 출력`

---

## 21.07.24

> - [1213 - 팰린드롬](https://www.acmicpc.net/problem/1213)
> - [7785 - 회사에 있는 사람](https://www.acmicpc.net/problem/7785)
> - [17413 - 팰린드롬](https://www.acmicpc.net/problem/17413)

`<1213>`

##### 팰린드롬이 될 수 있는 조건

> count가 홀수인 알파벳의 개수가 1 이하여야 한다.

```python
for data in datas_itmes: # datas_itmes는 알파벳순으로 정렬돼있음
    result += data[0] * (data[1] // 2)
print(result + odd_str + result[::-1])
```

`<7785>`

문제를 잘읽자! 정말 간단한 문제인데 사전역순으로 출력을 못봐서 조금 고민했음.

```python
for key in sorted(user.keys(), reverse = True):
    print(key)
```

`<17413>`

1. `공백이나 < 나오면 스택에 담겨있던 아이들을 차곡차곡 더한다.` -> `알아서 역순이 된다.`
2. `그리고 스택에 <가 들어있으면 >가 들어올때까지 모든 data들은 그냥 더한다.` -> `역순 x`

#### `파일명 정렬`

문자열 head, number, tail로 자르기

```python
head, number, tail = '', '', ''
for f in file:
            #만약 숫자인데 tail이 아직 없다면 계속 number
            if f.isdigit() and not tail:
                number += f
            else:
                # 아직 number가 나오기 전이라면 head
                if not number:
                    head += f
                # 이미 number가 있다면 tail
                else:
                    tail += f
```

자료구조는 `해시`를 사용했다.

```python
input_files.append({'head': head, 'lower-head': head.lower(),'number': number, 'tail': tail})
```

문제에서 힌트는 정렬에 `우선순위가 있다는 것`이었다.

1. `우선 head를 기준으로 정렬`
2. `head가 같다면 number를 기준으로 정렬`

따라서 해시에 key를 `head`, `number`, `tail`로 두고 value를 관리했다.
그런데 또 다른 조건이 `head는 대소문자 구분이 없다.`는 것이었다.

그래서 `lower-head`라는 key를 하나 더 만들었다.

그 다음 우선순위에 맞게 정렬을 하고, 출력을 하면 완성이다.

```python
for file in sorted(input_files, key=lambda x:(x['lower-head'], int(x['number']))):
        full_name_file = file['head'] + file['number'] + file['tail']
        answer.append(full_name_file)

    return answer
```

---

# 3주차 소감

> 문자열, 해시, 정렬이 생각보다 서로 서로 필요한 부분이 많아서 놀랬다. 파일명 정렬도 문자열 다루기만 생각하고 뽑은 문젠데 정렬, 해시 다 사용했다.
>
> 제일 뿌듯한 점은 해시랑 친해졌다는것, 정렬에 key를 여러개 사용할 수 있다는 것이다. 😀

---
