def solution(arr):
    min_idx = 0
    min_value = arr[min_idx]

    for i in range(1, len(arr)): # min_value를 갱신해주면서 최소일때의 index값 찾기
        if min_value > arr[i]:
            min_value = arr[i]
            min_idx = i
    answer = [arr[i] for i in range(len(arr)) if i != min_idx]
    return answer if answer else [-1] # result가 빈 배열이라면 [-1] 반환

def solution1(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]

print(solution([4, 3, 2, 1]))