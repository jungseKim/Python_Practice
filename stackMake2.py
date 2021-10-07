arr=[None]*10
size=len(arr)
tp=0
def put(arr,a):
    global tp
    if(tp<size):
        arr[tp]=a
        tp+=1
        return arr[tp-1]
    else :
        return 'over flow'
def get(arr):
    global tp
    if(tp>0):
        a=arr[tp-1]
        del arr[tp-1]
        tp-=1
        return a
    else:
        return 'empty is not'

print(put(arr,'a'))
print(get(arr))
print(put(arr,'b'))
print(arr)