def count_alive(board):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                cnt += 1
    return cnt

def solution(board, skill):
    for type, r1, c1, r2, c2, degree in skill:
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if type == 1:
                    board[i][j] -= degree
                else:
                    board[i][j] += degree
    return count_alive(board)

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))

#   for type, r1, c1, r2, c2, degree in sorted(skill, key=lambda x: (x[1], x[2], x[3], x[4])):
#         if stack and stack[-1][1:5] == [r1, c1, r2, c2]:
#             r11, c11, r22, c22 = stack[1:]
#             if type == 1:
#                 stack[-1][1:5] = [r11 + r1, c11 + c1, r22 + r2, c22 + c2]
#             else:
#                 stack[-1][1:5] = [r11 - r1, c11 - c1, r22 - r2, c22 - c2]
#         else:
#             stack.append([type, r1, c1, r2, c2, degree])