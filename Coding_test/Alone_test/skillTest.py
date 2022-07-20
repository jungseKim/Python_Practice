def solution(nums):
	arr=[]
	size=len(nums)
	for index in range(size-2):
		for x in nums[index+2:]:
			arr.append(nums[index]+nums[index+1]+x)
	for x in nums:
		temp=nums[:]
		temp.remove(x)
		while temp:
			arr.append(temp.pop())
	# 이거 그냥 차례대로 하면 될듯 
	return arr
print(solution([1,2,7,6,4]))