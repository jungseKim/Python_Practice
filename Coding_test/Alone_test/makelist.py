def solution(n):
    temp = str(n)
    answer = [int(s) for s in temp]
#     answer = map(int, [s for s in temp])
#     맵은 지정된 함수로 처리해 주는거임 근데 함수가 int
    answer.reverse()
#     reverse는 값을 반환안하고 reversed는 내장함수로 값을반환해준다
    print(answer)
    return answer


print(

    solution(1232)
)
