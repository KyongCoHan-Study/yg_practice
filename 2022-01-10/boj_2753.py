a = input()
a = int(a)

if ((a%4 == 0) &(a % 100 != 0)) or (a%400 == 0):
    print('1')
else:
    print('0')
    