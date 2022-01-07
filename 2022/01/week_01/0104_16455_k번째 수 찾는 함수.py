def kth(a, k):
    pivot = a[(len(a) + 1) // 2 - 1]
    left, mid, right = [], [], []
    for num in a:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)
    # print("left:", left, "\tmid:", mid, "\tright:", right, "\tk:", k)
    if k < len(left):
        return kth(left, k)
    elif k == len(left):
        return left[-1]
    elif k < len(left) + len(mid):
        return mid[0]
    else:
        return kth(right, k - len(left) - len(mid))

print(kth([3, 5, 1, 2, 9, 6, 4, 7, 5], 4))