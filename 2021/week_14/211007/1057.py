if __name__ == "__main__":
    import math

    n, target1, target2 = map(int, input().split())
    nums = [i for i in range(1, n + 1)]

    targets = set((target1, target2))

    for round in range(1, math.ceil(math.log2(n)) + 1):
        # round마다 반씩 사라짐
        winner = []
        
        for i in range(1, len(nums) + 1, 2):
            a = nums[i - 1]
            # 같이 스타 할 사람이 없으면 부전승
            if i == len(nums):
                winner.append(a)
                break
            # 같이 싸울 사람 있음
            b = nums[i]
            # target안에 a, b가 포암 됐을때
            if a in targets or b in targets:
                if set((a, b)) == targets: # a, b 가 target들이면 종료
                    print(round)
                    quit()
                elif a in targets: winner.append(a)
                elif b in targets: winner.append(b)
            # target이 아닌 사람들은 그냥 앞에 온 사람들 이기게 해줌
            else:
                winner.append(a)
        # 살아남은 사람이 다음 게임 진출
        nums = winner