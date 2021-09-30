def solution(sizes):
    maxW = max([x[0] for x in sizes])
    maxH = max([x[1] for x in sizes])
    for w, h in sizes:
        if(h <= maxW and w <= maxH):
            maxH = w
    return maxH*maxW
