# sol 1

N, M = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            sum = arr[i]+arr[j]+arr[k]
            if sum <= M:
                ans = max(ans, sum)
                
print(ans)
            

# sol 2

from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
res = 0

for i in combinations(cards, 3) :
	tot = sum(i)

	if tot > res and tot <= m :
		res = tot

print(res)
