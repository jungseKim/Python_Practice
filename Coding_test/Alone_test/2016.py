def solution(a, b):
    temp = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    from datetime import date
    answer = date(2016, a, b).weekday()
    return temp[answer]


print(solution(5, 24))
