a=int(input())
arr=[input() for i in range(a)]
temp={}
for x in arr:
   if(temp.get(x)):
        temp[x]=temp[x]+1
   else:
       temp[x]=1
max=0
title=''
for x in temp:
    if(temp[x]==max):
       if( x<title):
           title=x
    if(temp[x]>max):
        max=temp[x]
        title=x
print(title)