def hanoi(n, src, dst) :
	mid = 6-src-dst

	if n ==1 :
		print(src, dst)
		return
	else :
		hanoi(n-1, src, mid)
		print(src, dst)
		hanoi(n-1, mid, dst)

n = int(input())
print(2**n-1)
hanoi(n,1,3)


