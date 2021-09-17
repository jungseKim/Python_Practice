a=input()
temp={}
for i in a:
    sum=i.upper()
    if(temp.get(sum)):
        temp[sum]=temp[sum]+1
    else:
        temp[sum]=1
sum=0
result=''
for i in temp:
    if(temp[i]>sum):
        sum=temp[i]
        result=i

for i in temp:
    if(temp[i]==sum and i!=result):
        result='?'
print(result)