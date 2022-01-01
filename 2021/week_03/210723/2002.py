import sys
N = int(sys.stdin.readline())
cars = [sys.stdin.readline().rstrip() for _ in range(N)]
count = 0

for _ in range(N):
    car = sys.stdin.readline().rstrip()
    if car == cars[0]: # 들어간 순서가 맞으면
        cars = cars[1:] # cars에서 첫번째 차는 빼준다.
    else:
        car_index = cars.index(car) # 순서가 맞지 않으면
        cars = cars[:car_index] + cars[car_index + 1:] # 그 차는 쏘옥 빼고 다시 list 뽑음
        count += 1

print(count)