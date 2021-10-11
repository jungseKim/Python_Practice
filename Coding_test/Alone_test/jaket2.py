def solution(n, lost, reserve):
    temp=list(set(lost)-set(reserve))
    temp2=list(set(reserve)-set(lost))
    print(temp,temp2)

    for x in temp[:]:
        if(x+1 in temp2):
            temp2.remove(x+1)
            temp.remove(x)
        elif(x-1 in reserve ):
            temp2.remove(x-1)
            temp.remove(x)
    return n-len(temp)
print(solution(5, [2, 4], [3]))