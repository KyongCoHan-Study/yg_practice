n = int(input())
arr = []

for i in range(n) :
	num = int(input())
	arr.append(num)


for i in range(n) :
	for j in range(n-i-1) :
		if arr[j] > arr[j+1] :
			arr[j], arr[j+1] = arr[j+1], arr[j]

for i in arr :
	print(i)

