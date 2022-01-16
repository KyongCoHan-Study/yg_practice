import sys
input = sys.stdin.readline

N = int(input())
arr = list(list(map(int, input().split())) for _ in range(N))
arr = sorted(arr, key = lambda x: (x[1],x[0]))

for x, y in arr:
    print(x, y)
