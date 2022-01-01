def r_arr(dict):
    arr = []
    for k, v in (dict):
        for _ in range(v):
            arr.append(k)
    return arr

def solution(p, q):
    answer = []
    from itertools import combinations
    from collections import Counter
    for a, b in zip(p, q):
        flag = False
        arra, arrb = r_arr((Counter(a) - Counter(b)).items()), r_arr((Counter(b) - Counter(a)).items())
        graph = list(map(list, combinations(arra, 2)))
        for nums in list(combinations(graph, len(arrb))):
            for i, j in nums:
                arra = Counter(arra) - Counter([i, j])
            for i, j in nums:
                arra = arra + Counter([i + j])
            if Counter(arrb) == Counter(arra):
                flag = True
                break
        answer.append(flag)
    return answer

p = [[4,3,3],[1,2,3],[3,2,4]]
q = [[5,5],[5,1],[1,8]]
print(solution(p, q))

# 문제 설명
# 정수로 이루어진 두 집합 x, y가 주어졌을 때, 당신은 다음과 같은 과정을 통하여 x를 y와 동일하게 만들 수 있는지 알고 싶습니다.

# x의 임의의 두 수를 제거한 뒤, 그 둘을 합친 수를 다시 넣습니다.
# 예를 들어, x = [5,3,2,2,1], y = [7,2,4] 라면, x를 다음과 같은 과정을 거쳐 y로 만들 수 있습니다.

# [5,3,2,2,1] → [7,3,2,1] (5, 2 선택) → [7,2,4] (3, 1 선택)
# 이러한 x와 y가 여러 개 담긴 2차원 정수 배열 p와 q가 매개변수로 주어집니다. 각 경우에 대해서 x를 y로 만들 수 있으면 참값, 아니면 거짓값을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# p의 길이 = q의 길이
# 1 ≤ y의 길이 ≤ x의 길이 ≤ 20
# 1 ≤ x, y의 모든 수 ≤ 10,000,000
# x의 모든 수의 합 = y의 모든 수의 합
# 1 ≤ p의 각 행의 길이(= 각 x의 길이)의 합 ≤ 40

# 입출력 예
# p	q	result
# [[5,3,2,2,1]]	[[7,2,4]]	[true]
# [[4,3,3],[1,2,3],[3,2,4]]	[[5,5],[5,1],[1,8]]	[false,true,false]
