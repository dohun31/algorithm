def solution(lottos, win_nums):
    score = [6, 6, 5, 4, 3, 2, 1]
    cnt, zero_cnt = 0, lottos.count(0)
    for lotto in lottos:
        if lotto in win_nums:
            cnt += 1
    return [score[cnt + zero_cnt], score[cnt]]

if __name__ == "__main__":
    lottos = [44, 1, 0, 0, 31, 25]
    win_nums = [31, 10, 45, 1, 6, 19]
    print(solution(lottos, win_nums))