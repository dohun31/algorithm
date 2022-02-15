def back_tracking(nowv):
    nowv = str(nowv)
    for idx in range(len(nowv) - 1):
        if not int(nowv[idx] > nowv[idx + 1]):
            return False
    return True

if __name__ == "__main__":
    n = int(input())
