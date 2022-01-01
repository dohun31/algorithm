def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    return str(int(''.join(numbers)))

if __name__ == "__main__":
    numbers = [383, 38]
    print(solution(numbers))