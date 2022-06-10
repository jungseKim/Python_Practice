from re import L


n,k=map(int,input().split())
arr=[input().split() for x in range(n)]
arr.sort(key=lambda x: -int(x[1]))
c=[int(input()) for x in range(k)]
c.sort(reverse=True)
sum=0
for x in range(len(arr)):
	if len(c)==0:
		break
	for y in range(len(c)):
		if c[y]>=int(arr[x][0]):
			sum=sum+int(arr[x][1])
			c.pop(y)
			break
print(sum)
