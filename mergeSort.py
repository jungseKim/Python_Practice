def merge(arr, arr2):
    temp = []
    while True:
        if(len(arr) == 0 or len(arr2) == 0):
            temp.extend(arr)
            temp.extend(arr2)
            return temp
        if(arr[0] > arr2[0]):
            temp.append(arr2.pop(0))
        else:
            temp.append(arr.pop(0))


def merge_sort(list):
    if(len(list) == 1):
        return list
    else:
        arr = merge_sort(list[0:int(len(list)/2)])
        arr2 = merge_sort(list[int(len(list)/2):])
        return merge(arr, arr2)


print(merge_sort([1, 3, 7, 2, 2, 3, 4, 23, 22, 2, 2, 4, 6, 8]))
