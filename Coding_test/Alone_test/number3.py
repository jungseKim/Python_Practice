def solution(n, m):
    answer = [0, 0]
    if(n > m):
        n, m = m, n
    # print([i for i in range(1, n+1) if n % i == 0 and m % i == 0])
    answer[0] = max([i for i in range(1, n+1) if n % i == 0 and m % i == 0])
    temp = n*m
    for x in range(1, temp):
        if(x % n == 0 and x % m == 0 and temp > x):
            temp = x
            break
    answer[1] = temp
    print(answer)
    return answer


solution(3, 12)
