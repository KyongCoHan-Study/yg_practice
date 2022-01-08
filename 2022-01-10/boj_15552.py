import sys

T = int(sys.stdin.readline())

for i in range(T):
    line = sys.stdin.readline()
    split_line = line.split(' ')
    a = int(split_line[0])
    b = int(split_line[1])
    print(a + b)

