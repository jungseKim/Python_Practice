a=int(input())
si=[int(input()) for _ in range(a)]

temp=[0]*(max(si)+1)
temp[0]=[1,0]
temp[1]=[0,1]

for x in range(2,max(si)+1):
    ri=temp[x-1][0]+temp[x-2][0]
    li=temp[x-1][1]+temp[x-2][1]
    temp[x]=[ri,li]
print(temp)
for x in si:
    print(temp[x][0],temp[x][1])
    