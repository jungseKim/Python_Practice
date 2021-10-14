a,b=map(int,input().split())
temp=[x for x in range(a)]
temp[0],temp[1]=0,0
for x in range(a):
    if(temp[x]!=0):
        for y in range(x*2,a,x):
            temp[y]=0
temp=[x for x in temp if x!=0]
for x in temp:
    check=False
    for y in temp:
        if(x*y==a):
            if(x<b or y<b):
                print('BAD',min(x,y))
            else:
                print('GOOD')
            check=True
    if(check):
        break