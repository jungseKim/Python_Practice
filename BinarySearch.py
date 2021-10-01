list = [1, 3, 6, 9, 12, 15, 18, 21]
a = int(input())


def search(arr):
    global a
    print(len(arr), arr)
    if(arr[int(len(arr)/2)] == a):
        return "true"
    if(len(arr) == 1):
        return "false"
    elif(arr[int(len(arr)/2)] > a):
        return search(arr[0:int(len(arr)/2)])
    else:
        return search(arr[int(len(arr)/2):])


print(
    search(list))
