# list문제에서 메모리 제한이 있다면 미리 틀을 만들어놓은 후 증감식으로 개수를 세는 것이 상당히 유리하다.
import sys
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(10001)]

for i in range(N):
    num = int(input())
    arr[num] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)1
