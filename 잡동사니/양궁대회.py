class Factory:
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance;
    
    def create_next_if_win(_, current, next_n):
        new_visited = current.visited[::]
        new_visited[current.i] = next_n + 1;
        new_visited[-1] = 0
        return Node(current.i + 1, new_visited)
    
    def create_next_if_tie(_, current, next_n):
        new_visited = current.visited[::]
        new_visited[current.i] = next_n
        new_visited[-1] = 0
        return Node(current.i + 1, new_visited)
    
    def create_next_if_lose(_, current):
        return Node(current.i + 1, current.visited[::])

class Node:
    def __init__(self, index, visited):
        self.i = index
        self.visited = visited
    
    def get_diff_score(self, apeach):
        score = 0
        for i in range(10):
            if self.visited[i] > apeach[i]:
                score += 10 - i
            else:
                if apeach[i] > 0:
                    score -= 10 - i
        return score

def solution(n, info):
    def backtrack(node):
        print(node.i, node.visited)
        if node.i == 10:
            return node;
        
        node_factory = Factory()
        lose_node = node_factory.create_next_if_lose(node)
        tie_node = node_factory.create_next_if_tie(node, info[node.i])
        win_node = node_factory.create_next_if_win(node, info[node.i])
        comparable = lambda x: (x.get_diff_score(info), x.visited[::-1])

        if sum(win_node.visited) <= n:
            return max(backtrack(win_node), backtrack(lose_node), backtrack(tie_node), key = comparable)
        elif sum(tie_node.visited) <= n:
            return max(backtrack(tie_node), backtrack(lose_node), key = comparable)
        else:
            return backtrack(lose_node)
    
    ryan = backtrack(Node(0, [0] * 11))
    ryan.visited[-1] = n - sum(ryan.visited[:-1])

    return ryan.visited if ryan.get_diff_score(info) > 0 else [-1]

print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))