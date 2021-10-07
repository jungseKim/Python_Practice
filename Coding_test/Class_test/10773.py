a=int(input())
arr=[]
for x in range(a):
    h=int(input())
    if(h==0 and len(arr)>0):
        arr.pop()
    else:
        arr.append(h)
result=sum(arr)
print(result)