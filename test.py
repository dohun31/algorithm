def is_prime(n):
    import math
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def make_n_mod(n, k):
    j = ''
    while n > 0 :
        n, mod = divmod(n, k)
        j += str(mod)
    return j[::-1]

def solution(n, k):
    result1 = make_n_mod(n, k)
    s=result1.split('0')

    count = 0
    for i in s:
        if i.isdigit() and is_prime(int(i)):
            count += 1
    return count

print(solution(110011, 10))
# 제가 더 감사합니다 ㅎ ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
#고생하셧습니다 슨생님 내일 다시 풀어볼게요
# 그러게요 화이팅
# 정리 끝
# 도움이 되셨길 이거 신기하다 라이브 쉐어
# 네 좋은 경험 시켜주셔서 감사합니다
# 그럼 얼른 부산와서 밥이나 사주세요 ㅎㅎ
# 아 이제 누워야겠따
# 복습 꼭 하세요
# 소수 알고리즘이랑
# 진법 바꾸기랑
# 슬라이싱이랑
# 뭐 볼거 많네
# 화이팅