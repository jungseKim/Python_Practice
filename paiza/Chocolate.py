from tabnanny import check


n,m=map(int,input().split())
arr=[list(map(int,input().split())) for x in range(n)]

answer=[]
check=True
while len(arr)>0:
	temp=arr.pop(0)
	min=temp.pop(0)
	max=sum(temp)
	temp.pop()
	index=0
	for i,x in enumerate(temp):
		if min==max:
			check=True
			index=0
			tmep2=["A" for x in range(i+1)]
			tmep2.extend(["B" for x in range(m-i-1)])
			answer.append("".join(tmep2))
			break;
		min=min+x
		max=max-x
	if min!=max:
		print("No")
		check=False
		break
	else:
		tmep2=["A" for x in range(m-2)]
		tmep2.append("B")
		# tmep2.extend(["B" for x in range(m-i-1)])
		answer.append("".join(tmep2))
		
if check:
	print("Yes")
	for x in answer:
		print(x)