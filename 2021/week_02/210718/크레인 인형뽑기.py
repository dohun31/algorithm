board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution1(board, moves):
    moves.reverse() # 스택으로 사용하려고 reverse 해서 뒤짚음.
    stack = []
    answer = 0
    while moves:
        move = moves.pop()
        for list in board: # 한 행씩 탐색
            if list[move - 1] != 0: # 원하는 열에 인형이 있으면
                stack.append(list[move - 1]) # stack에 넣고
                list[move - 1] = 0 # 인형을 없앰
                break
        if len(stack) > 1 and stack[-1] == stack[-2]: # 스택에 인형이 두 개 이상 있고, 젤 상단 2개가 같으면
            stack.pop() # 인형 두 개 터짐 펑펑
            stack.pop()
            answer += 2 # 그리고 터진 인형만큼 +
    return answer


def solution(board, moves):
    stack = []
    answer = 0
    for move in moves:
        for row_board in board:
            if row_board[move - 1] != 0:
                stack.append(row_board[move - 1])
                row_board[move - 1] = 0
                break
        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            answer += 2
    return answer

result = solution(board, moves)
print(result)