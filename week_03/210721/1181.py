import sys
datas = {sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline()))}
print('\n'.join(sorted(datas, key=lambda x : (len(x), x)))) # 길이 짧은거 우선, 같다면 사전식