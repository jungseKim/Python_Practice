def solution(N, stages):
    answer = {int(x): 0 for x in range(1, N+2)}
    M = len(stages)
    for x in stages:
        if(M > 0):
            answer[x] = x/M
            M = M-x
    sorted_answer = sorted(answer.items())
    return sorted_answer
