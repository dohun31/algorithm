import sys

def expected_time(d):
    if d >= 100:
        return a
    nowv = d * 0.01 * a + (100 - d) * 0.01 * (a + expected_time(d * (1 + k * 0.01)))
    return nowv

if __name__ == "__main__":
    # 끝말잇기 한 판  -> a 분
    # 현재 자신이 이길 확률 -> d%
    # 집중 모드 -> 패배할때마다 이전에 비해 K% 오름
        # 100% 넘으면 다음판 부터는 반드시 승리
    a, d, k = map(int, sys.stdin.readline().split())
    print("{:.10f}".format(expected_time(d)))
