n = int(input())
arr = [[' ' for _ in range(n)] for _ in range(n)]

def star(n):
    global arr

    if n == 3:
        arr[0][:3] = arr[2][:3] = ['*', '*', '*']
        arr[1][:3] = ['*', " ", '*']
        return
    else:
        star(n//3)
        a = n//3

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                else:
                    for k in range(a):
                        arr[a*i + k][a*j:a*(j+1)] = arr[k][:a]

star(n)

for i in arr:
    for j in i:
        print(j, end = '')
    print()
