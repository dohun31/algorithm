if __name__ == "__main__":
    num_cnt = [0] * 9
    nums = input()

    for num in nums:
        if num == '9':
            num = '6'
        num_cnt[int(num)] += 1
    
    num_cnt[6] = (num_cnt[6] + 1) // 2
    print(max(num_cnt))