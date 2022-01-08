n = int(input())
made = n
cnt = 0
while True:
    made = (made//10 + made % 10) % 10 + 10 * (made % 10)
    cnt += 1
    if made == n:
        print(cnt)
        break


