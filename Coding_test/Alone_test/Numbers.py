def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        temp = []
        for x in range(1, i+1):
            if i % x == 0:
                temp.append(x)
        if len(temp) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
