# a,b=map(int,input().split())
# temp=[x for x in range(1,b+1)if x%2!=0]
# temp=set(temp)

# for x in temp:
#    if(x!=1):
#         temp=temp-set(i for i in range(x,b+1,x) if i!=x)

# for x in temp:
#     if(x>=a):
#         print(x)

a,b=map(int,input().split())
temp=[x for x in range(b+1)]
temp[0],temp[1]=0,0

for x in range(b+1):
    if(temp[x]!=0):
        for y in range(x*2,b+1,x):
            temp[y]=0
for x in temp:
    if(x>=a and x!=0):
        print(x)
                
