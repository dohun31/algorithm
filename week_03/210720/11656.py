import sys
data = sys.stdin.readline().rstrip()
print('\n'.join(sorted([data[i:] for i in range(len(data))])))