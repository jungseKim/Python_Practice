# stack make
size=10
# arr=[None for i in range(10)]
# arr=[None]*10
arr=[0]*size
# print(len(arr))
def push(arr,a):
    if(len(arr)<size):
        arr.append(a)
        return arr
    else:
        return 'stack overflow'
def pop(arr):
    if(len(arr)>0):
        a=arr[-1]
        del arr[-1]
        return a  
    else:
        return 'stack empty'
print(pop(arr))
print(push(arr,'a'))