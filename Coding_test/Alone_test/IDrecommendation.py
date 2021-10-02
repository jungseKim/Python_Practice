def solution(new_id):
    new_id = new_id.lower()
    arr = ['.', '-', '_']
#      소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)
    for x in new_id:
        if(arr.count(x) == 0 and not(96 < ord(x) < 123)):
            new_id = new_id.replace(x, '')
    new_id = new_id.replace('..', '.')

    if(len(new_id) > 1):
        if(new_id[-1] == '.'):
            new_id = new_id[0:-1]
        if(new_id[0] == '.'):
            new_id = new_id[1:]
    if(len(new_id) == 0):
        new_id = 'a'
    if(len(new_id) > 15):
        new_id = new_id[0:15]
    if(new_id[-1] == '.'):
        new_id = new_id[0:-1]
    while len(new_id) <= 2:
        new_id = new_id+new_id[-1]
    return new_id


print(solution("=.="))
