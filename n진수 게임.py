class Factory:
    n = 1
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_next_node(self, node):
        if node.i == len(node.arr) - 1:
            print("new")
            print(node.arr, node.i, node.value)
            return Node(0, node.value + 1, self.__get_change_nmod(node.value + 1))
        node.i += 1
        return node
    
    def __get_change_nmod(self, value):
        stack = []
        while value > 0:
            value, mod = divmod(value, self.n)
            stack.append(self.__get_nmod_number(mod))
        return stack[::-1]
    
    def __get_nmod_number(_, mod):
        if 0 <= mod < 10: return mod
        elif mod == 10: return 'A'
        elif mod == 11: return 'B'
        elif mod == 12: return 'C'
        elif mod == 13: return 'D'
        elif mod == 14: return 'E'
        elif mod == 15: return 'F'


class Node:
    def __init__(self, i = 0, value = 0, arr = [0]):
        self.i = i
        self.value = value
        self.arr = arr

def solution(n, t, m, p):
    node_factory = Factory()
    node_factory.n = n
    node = next_node = Node()

    answer = ""
    for i in range(t * m):
        print('---')
        if i % m == p - 1:
            print("my turn")
            answer += str(node.arr[node.i])
            print(answer)
        print("---")
        print()
        node = next_node
        next_node = node_factory.get_next_node(node)
    return answer

print(solution(16, 16, 2, 2))