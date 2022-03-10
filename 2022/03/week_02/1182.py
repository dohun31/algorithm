import sys

def find_all_case(idx, arr):
    if idx == n - 1:
        if arr and sum(arr) == s:
            global cnt
            cnt += 1
        return
    next_idx = idx + 1
    find_all_case(next_idx, arr + [numbers[next_idx]])
    find_all_case(next_idx, arr)

if __name__ == "__main__":
    n, s = map(int, sys.stdin.readline().split())
    numbers = list(map(int, sys.stdin.readline().split()))
    
    cnt = 0
    find_all_case(-1, [])
    print(cnt)