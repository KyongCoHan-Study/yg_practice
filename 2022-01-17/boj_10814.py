import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    a, b = input().split()
    arr.append([int(a),b])

arr = sorted(arr, key = lambda x:x[0] )

for a, b in arr:
    print(a, b)
