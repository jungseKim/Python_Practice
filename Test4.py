# def go(a):
#     if(a < 10):
#         return go(a+1)
#     else:
#         return 10


# print(go(1))
# str = "hellowjung"
# print(str[1:4])

# def solution(answers):
#     arr=[[1,2,3,4,5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
#     answer = [0,0,0]
#     for index,x in enumerate(answers):
#         if(arr[0][index%len(arr[0])]==x):
#             answer[0]=answer[0]+1
#         if(arr[1][index%len(arr[1])]==x):
#             answer[1]=answer[1]+1
#         if(arr[2][index%len(arr[2])]==x):
#             answer[2]=answer[2]+1
#     return sum(answer)
# print(solution([1,2,3,4,5]))

# temp = [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9],
#         ['*', 0, '#']]
# print(temp.index([1, 2, 3]))

# a, b = map(int, input().split())
# print(a+b)

# 1) integer: 정수형
#     2) float: 실수형
#     3) string: 문자형
#     4) boolean: 불리언
# //단일값은 이것밖에 없음

# temp = [1, 2, 3]
# temp.insert(0, 6)
# temp.insert(len(temp), 0)
# print(temp)

# temp = """hellow
# my friend"""
# print(list(temp))

# a = int(input())
# print('fuck' if a > 0 else 'me')
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [1, 2, 3, 4, 5, 6, 7, 9]
# for a, b in zip(a, b):
#     print(a, b)
# a = [1, 2, 3, 'd', 3]

# print(type(1))


# def sumj(*list):
#     #     b = [x for x in list if type(x) is int]
#     #     print(b)
#     for x in list:
#         # print(x)
#         if(type(x) is int):
#             print(x)
#         else:
#             print('no')


# sumj(*a)


a = [1, 3, 6, 9, 12, 15, 18, 21]
b = 8


def binary(v, a, low, high):
    mid = (low+high)//2
    if(low > high):
        return "false"
    if(a[mid] == v):
        return mid
    if(a[mid] > v):
        return binary(v, a[:mid], low, mid-1)
    else:
        return binary(v, a[mid:], mid+1, high)


print(binary(b, a, 0, len(a)))
