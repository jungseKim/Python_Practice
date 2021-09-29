def solution(numbers):
    answer = 45
    for x in numbers:
        answer -= x
    return answer
