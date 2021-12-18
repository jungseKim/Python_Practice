def solution(n, arr1, arr2):
    answer = [[] for i in range(n)]
    for index, (x, y) in enumerate(zip(arr1, arr2)):
        x = format(x, 'b')
        y = format(y, 'b')
        print(x, y)
        x = ''.join([' ']*(n-len(x)))+x
        y = ''.join([' ']*(n-len(y)))+y
        for z, h in zip(x, y):
            if z == '1' or h == '1':
                answer[index].append('#')
            else:
                answer[index].append(' ')
    for index, x in enumerate(answer):
        answer[index] = ''.join(x)
    return answer


# zfill rjust 사용해서 풀어보기
solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
