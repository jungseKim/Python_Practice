
def draw(arr,last):
	if arr[last]!=None:
		return last+" <- "+draw(arr,arr[last])
	return last

def bellman(state,start,last):
	# v=len(state)
	value,next={},{}
	for node in state:
		value[node]=float("inf")
		next[node]=None
	value[start]=0

	# for sd in range(v):
	for index,Cnode in enumerate(state) :
		for Nnode in state[Cnode]:
			if value[Nnode]>value[Cnode]+state[Cnode][Nnode]:
				value[Nnode]=value[Cnode]+state[Cnode][Nnode]
				next[Nnode]=Cnode
		print("count",index)	
		print(draw(next,last));
	return next

state={
	'A':{'B':9,'C':2},
	'B':{'D':3,'A':9,'C':6,'E':1},
	'C':{'A':2,'B':6,'F':9,'D':2},
	'D':{'C':2,'B':3,'E':5,'F':6},
	'E':{'B':1,'D':5,'F':3,'G':7},
	'F':{'D':6,'E':3,'G':4,'C':9},
	'G':{'E':7,'F':4}
}


print("answer",draw(bellman(state,"A","G"),"G"))

