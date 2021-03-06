k = int(input())
building_num = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def find_locate(arr, dep):
    arr_len = len(arr)
    if arr_len != 1:
        tree[dep].append(arr[arr_len // 2]) # 현재 arr의 루트 노드를 현재 깊이에 push
        find_locate(arr[:arr_len // 2], dep + 1) # 현재 루트 노드의 왼쪽 자식
        find_locate(arr[arr_len // 2 + 1:], dep + 1) # 현재 루트 노드의 오른쪽 자식
    else: # 제일 마지막 깊이일때
        tree[dep].append(arr[0])

find_locate(building_num, 0)

for t in tree:
    print(*t)