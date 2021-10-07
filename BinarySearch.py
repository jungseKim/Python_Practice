list=[1, 3, 6, 9, 12, 15, 18, 21 ]
x=int(input())
start=0
end=len(list)-1
# 리턴 만 다시 짜서 작성 해보기
def searh():
    global x,start,end,list
    middle=int((start+end)/2)
    if(start>=end):
        print('no')
        return
    if(list[middle]==x or list[middle+1]==x):
        print("trure")
        return "true"
    elif(list[middle]<x):
        start=middle
        searh()
    else:
        end=middle
        searh()
searh()
print()