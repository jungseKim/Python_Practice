



    


a,b=map(int,input().split(' '))
arr1={input() for x in range(a)}
arr2={input() for x in range(b)}
temp=arr1&arr2
temp2=sorted(temp)
print(len(temp))
for i in temp2:
    print(i)

