i = int(input())
arr = [0 for n in range(i)]


for cnt in range(0,i):
    a, b = input().split()
    a = int(a)
    b = int(b)
    arr[cnt] = a + b

for cnt in range(0,i):
    print(arr[cnt])
