k = int(input())
building_num = list(map(int, input().split()))
tree = [[] for _ in range(k)]

def find_locate(arr, dep):
def find_locate(arr, dep):
    arr_len = len(arr)
    if arr_len != 3: # 길이가 3이 아니면
        tree[dep].append(arr[arr_len // 2]) # 현재 arr의 루트 노드를 현재 깊이에 push
        find_locate(arr[:arr_len // 2], dep + 1) # 현재 루트 노드의 왼쪽 자식
        find_locate(arr[arr_len // 2 + 1:], dep + 1) # 현재 루트 노드의 오른쪽 자식
    else: # 제일 마지막 깊이일때
        tree[dep].append(arr[1]) # 부모 노드
        tree[dep + 1].append(arr[0]) # 왼쪽 자식
        tree[dep + 1].append(arr[2]) # 오른쪽 자식

find_locate(building_num, 0)

for t in tree:
    print(*t)