def merge(arr, arr2):
    temp = []
    if(len(arr) == 1):
        if(arr[0] > arr2[0]):
            temp.append(arr2[0])
        else:
            temp.append(arr[0])
        return temp
#     print(arr, arr2)
    for x, y in arr, arr2:
        if(x > y):
            temp.append(y)
            arr2.remove(y)
        else:
            temp.append(x)
            arr.remove(x)
    if(len(arr) != 0):
        temp.extend(arr)
    if(len(arr2) != 0):
        temp.extend(arr2)

    print(temp)
    return temp


def merge_sort(list):
    if(len(list) == 1):
        return list
    else:
        arr = merge_sort(list[0:int(len(list)/2)])
        arr2 = merge_sort(list[int(len(list)/2):])
        print(arr)
        return merge(arr, arr2)


print(merge_sort([1, 3, 7, 4, 6, 8]))
