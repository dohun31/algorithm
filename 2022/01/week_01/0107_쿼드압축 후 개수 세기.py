def check(arr):
    target = arr[0][0]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if target != arr[i][j]:
                return False, target
    return True, target

def solution(arr):
    result = [0, 0]
    # 한 개만 남으면 반환
    if len(arr) == 1:
        return [0, 1] if arr[0][0] == 1 else [1, 0]
    # 체크
    ch_result, value = check(arr)
    # true면 value 반환
    if ch_result:
        return [0, 1] if value == 1 else [1, 0]
    # 4등분 할 stack 배열 선언
    stacks = [[], [], [], []]
    # 4등분하기
    for i in range(len(arr)):
        if i < len(arr) // 2:
            stacks[0].append(arr[i][:len(arr) // 2])
            stacks[1].append(arr[i][len(arr) // 2:])
        else:
            stacks[2].append(arr[i][:len(arr) // 2])
            stacks[3].append(arr[i][len(arr) // 2:])
    # stack들 돌면서 결과 갱신하기
    for stack in stacks:
        nowv = solution(stack)
        result[0] += nowv[0]
        result[1] += nowv[1]
    return result


if __name__ == "__main__":
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    print(solution(arr))