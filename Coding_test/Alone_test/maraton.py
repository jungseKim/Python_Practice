def solution(participant, completion):
    temp1 = set()
    temp2 = set()
    for x in participant:
        if(x in temp1):
            temp2.add(x)
        else:
            temp1.add(x)
    temp3 = set()
    temp4 = set()
    for x in completion:
        if(x in temp3):
            temp4.add(x)
        else:
            temp3.add(x)
    a = temp1-temp3
    b = temp2-temp4
    temp = list(a | b)
    return temp[0]


print(solution(["mislav", "stanko", "mislav", "ana"],
      ["stanko", "ana", "mislav"]))
print(solution(['a', 'b'], ['a']))
