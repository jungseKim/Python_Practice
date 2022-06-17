n,m=map(int,input().split())

arr=list(map(int,input().split()))
arr2=list(map(int,input().split()))

answer=[[0]*m for x in range(n)]
answer[0][0],answer[0][1]=arr[0],arr[1]
answer[1][0],answer[1][1]=arr2[0],arr2[1]

for i in range(2):	
	for x in range(m-2):
		answer[i][x+2]=answer[i][x+1]+answer[i][x+1]-answer[i][x]

for i in range(n-2):	
	for x in range(m):
		answer[i+2][x]=answer[i+1][x]+answer[i+1][x]-answer[i][x]

for index,x in enumerate(answer):
	for index2,i in enumerate(x):
		if index2<m-1:
			print(i,end=" ")
		else:
			print(i)
	# if index<n:
	# 	print("")
