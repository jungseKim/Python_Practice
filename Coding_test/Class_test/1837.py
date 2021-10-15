a, b = map(int, input().split())
temp = [x for x in range(b)]
temp[0], temp[1] = 0, 0
for x in range(b):
    if(temp[x] != 0):
        # 문제1 a까지 돔
        for y in range(x*2, b, x):
            temp[y] = 0
temp = [x for x in temp if x != 0]
check = True
for x in temp:
    if(a % x == 0):
        print('BAD', x)
        check = False
        break
if(check):
    print('GOOD')

# for x in temp:
#     check = False
#     # 문제2 x * y를 할 필요가 없음 p % x == 0 이면 자동으로 몫이 소수
#     # 반복문 하나 더 안써도 된다는 의미
#     for y in temp:
#         if(x*y == a):
#             if(x < b or y < b):
#                 print('BAD', min(x, y))
#             else:
#                 print('GOOD')
#             check = True
#     if(check):
#         break
