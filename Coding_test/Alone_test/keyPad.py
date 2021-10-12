def solution(numbers, hand):
    answer = []
    match = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9],
             ['*', 0, '#']]
    left = [3, 0]
    right = [3, 2]

    for x in numbers:
        temp = [0, 0]
        for index, y in enumerate(match):
            if(x in y):
                temp = [index, y.index(x)]
        if(x in [1, 4, 7]):
            left = temp
            answer.append('L')
        elif(x in [3, 6, 9]):
            right = temp
            answer.append('R')
        else:
            l_fit = abs(left[0]-temp[0])+abs(left[1]-temp[1])
            r_fit = abs(right[0]-temp[0])+abs(right[1]-temp[1])
            if(r_fit == l_fit):
                if(hand == "right"	):
                    right = temp
                    answer.append('R')
                else:
                    left = temp
                    answer.append('L')
            elif(r_fit > l_fit):
                left = temp
                answer.append('L')
            else:
                right = temp
                answer.append('R')
    return ''.join(answer)
