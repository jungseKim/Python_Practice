
from re import L


def solution(n, info):
	# max=0
	answer = [0]*11
	temp=[0]*11
	# for index,x in enumerate(info):
	# 	if x==0 and n>0:
	# 		n=n-1
	# 		max=10-index
	# 		answer.ap
	# temp= [(((10-index))/(x+1))*x for index,x in enumerate(info)]
	for index,x in enumerate(info):
		temp[index]=((10-index))/(x+1)
		
		temp[index]=temp[index]+2-index/1.5
		# 	temp[index]=temp[index]+10-index-5

	print(temp)
	# while n>=0:
	# 	tmp = max(temp)
	# 	index = temp.index(tmp)
	# 	temp[index]=-1
	# 	value=info[index]
	# 	if n-value-1>=0:
	# 		n=n-value-1
	# 		answer[index]=value+1
	# 	else:
	# 		temp[index]=tmp		
		
	return answer;
print(solution(5,[0,0,1,2,0,1,1,1,1,1,1]))

