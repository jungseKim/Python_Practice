def solution(n):
    answer = [ x for x in str(n)]
    answer.sort(reverse=True)
    ap=''.join(answer)
    return int(''.join(answer))
    # revers는 값을 반환하지않아서 프린터에 안찍힘
    # reversed는 리스트 내장함수가 아니다
    # 조인 할때 문자열만 가능 인트형은 안된다
solution(19989)