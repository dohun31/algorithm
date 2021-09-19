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
            # 현재 높이가 이전의 높이보다 작을 동안 큰 직사각형 가능성 농후
            while stack and stack[-1][1] > h:
                w, tmp_h = stack.pop()
                print((idx - w) * tmp_h)
                ans = max(ans, (idx - w) * tmp_h)
            stack.append((w, h))
            print(stack)
        print(ans)