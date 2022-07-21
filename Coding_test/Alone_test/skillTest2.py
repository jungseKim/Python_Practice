# test1
def solution(s):
	str=s.lower()
	if str.count("p")==str.count("y"):
		return True
	return False

# test2
import datetime
def solution(a,b):
	arr=["FRI","SAT","SUN","MON","TUE","WED","THU"]
	start=datetime.datetime(2016,1,1)
	last=datetime.datetime(2016,a,b)
	answer=last-start
	return arr[(answer.days)%7]
print(solution(1,2))