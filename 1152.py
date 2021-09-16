a=input()
arr=a.split(' ')
if(len(arr[0])<1):
    del arr[0]
if(len(arr[-1])<1):
    del arr[-1]
print(len(arr))