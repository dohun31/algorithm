def solution(arr1, arr2):
    row1, col1, row2, col2 = len(arr1), len(arr1[0]), len(arr2),len(arr2[0])
    answer = []
    for i in range(row1):
        nowv1 = arr1[i]
        now_answer = []
        for j in range(col2):
            nowv2 = []
            for k in range(row2):
                nowv2.append(arr2[k][j])
            now_answer.append(sum([nowv1[i] * nowv2[i] for i in range(col1)]))
        answer.append(now_answer)
    return answer

if __name__ == "__main__":
    arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2 = [[5, 4], [2, 4], [3, 1]]
    print(solution(arr1, arr2))