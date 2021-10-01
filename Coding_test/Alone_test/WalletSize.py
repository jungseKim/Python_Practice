def solution(sizes):
    top = []
    low = []
    for x, y in sizes:
        if(x > y):
            top.append(x)
            low.append(y)
        else:
            low.append(x)
            top.append(y)

    return max(top)*max(low)
