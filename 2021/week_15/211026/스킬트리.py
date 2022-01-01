def solution(skill, skill_trees):
    count = 0
    for sk in skill_trees:
        stack = list(reversed(skill))
        for alpha in sk:
            if alpha in skill:
                if stack[-1] == alpha:
                    stack.pop()
                else:
                    break
        else:
            count += 1
    return count

if __name__ == "__main__":
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
    print(solution(skill, skill_trees))