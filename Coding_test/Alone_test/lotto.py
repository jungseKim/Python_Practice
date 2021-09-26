def solution(lottos, win_nums):
    min = len(set(lottos) & set(win_nums))
    max = min+lottos.count(0)
    answer = [6 if max == 0 else -(max-7), 6 if min == 0 else -(min-7)]
    return answer
