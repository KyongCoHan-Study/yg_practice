ia,b = input().split()

a = int(a)
b = int(b)

if( b < 45):
    b += 15
    if( a == 0):
        a = 23
    else:
        a -= 1
else:
    b -= 45
print(str(a) + " " +str(b))
