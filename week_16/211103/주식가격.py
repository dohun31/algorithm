def solution(prices):
    answer = [0 for _ in range(len(prices))]
    arr = [0]
    for i in range(1, len(prices)):
        new_arr = [i]
        for j in arr:
            if prices[i] >= prices[j]:
                new_arr.append(j)
            answer[j] += 1
        arr = new_arr
    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    print(solution(prices))