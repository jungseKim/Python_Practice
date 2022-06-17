from webbrowser import Galeon


n=int(input())
a,b=map(int,input().split())

arr=[True]*n
def go(x,a,b):
	global n
	global arr
	arr[x]=False
	if x+a<n:
		go(x+a,a,b)
	if x+b<n:
		go(x+b,a,b)
go(0,a,b)
print(arr.count(True))