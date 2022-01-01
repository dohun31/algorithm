import sys
N, M = map(int, sys.stdin.readline().split())
pokemons = {}

for i in range(N):
    pokemons[i + 1] = sys.stdin.readline().rstrip()
reversed_pokemons = dict(map(reversed, pokemons.items())) # 이름으로 도감 번호 접근 하기 위해서

for _ in range(M):
    order = sys.stdin.readline().rstrip()
    if order.isdigit(): # 숫자라면
        print(pokemons[int(order)]) # dict 형에서 도감 번호로 포켓몬 이름 출력
    else:
        print(reversed_pokemons.get(order)) # 아니면 포케못 이름으로 도감 번호 출력