if __name__ == "__main__":
    while True:
        n, *datas = map(int, input().split())
        # 종료 조건
        if n == 0:
            break
        ans, stack = 0, [] # 결과 저장할 ans, 높이들 쌓을 stack
        datas.append(0)
        for idx, h in enumerate(datas):
            w = idx
            while stack and stack[-1][1] > h:
                w, tmp_h = stack.pop()
                ans = max(ans, (idx - w) * tmp_h)
            stack.append((w, h))
        print(ans)