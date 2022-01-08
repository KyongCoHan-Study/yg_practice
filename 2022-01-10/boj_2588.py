a = input()
a = int(a)
b = input()
b = int(b)

x = a * (b % 10)
y = a * int((b % 100)/10)
z = a * int(b/100)
res = a * b
print(x, y, z, res, sep='\n')
