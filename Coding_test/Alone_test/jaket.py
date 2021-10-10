def solution(n, lost, reserve):
    a=lost.copy()
    lost=[x for x in lost if x not in reserve]
    reserve=[x for x in lost if x not in a]

    for x in lost[:]:
        if(x+1 in reserve ):
            reserve.remove(x+1)
            lost.remove(x)
        elif(x-1 in reserve ):
            reserve.remove(x-1)
            lost.remove(x)
    print(lost)
    return n-len(lost)
print(solution(5, [2, 4], [3]))