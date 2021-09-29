def solution(price, money, count):
    answer = 0
    temp = price
    for i in range(count):
        answer += temp
        temp += price
        print(answer)
    if((answer-money) < 0):
        return 0
    return answer-money


print(solution(3, 20, 4))
