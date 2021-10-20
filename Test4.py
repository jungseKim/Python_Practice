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


# a = [1, 3, 6, 9, 12, 15, 18, 21]
# b = 8


# def binary(v, a, low, high):
#     mid = (low+high)//2
#     if(low > high):
#         return "false"
#     if(a[mid] == v):
#         return mid
#     if(a[mid] > v):
#         return binary(v, a[:mid], low, mid-1)
#     else:
#         return binary(v, a[mid:], mid+1, high)
#  prin

# print(binary(b, a, 0, len(a)))

# a = list(map(int, input().split()))
# a.insert(0, 3)
# del a[:]
# # print(a)
# a, b = map(int, input().split())
# print('ddd') if a+b > 0 else print('np')


# def print2(list):
#     list = [x for x in list if x % 2 == 0]
#     for x in list:
#         print(x)


# print2([1, 2, 3, 4, 5, 6, 7, 8, 9])
# list = [x*3 for x in range(1, 10)]
# print(list)

# def min_int(*dd):
#     return min(dd)


# print(min_int(12323, 32323, 3232, 3, 2, 32, 3, 23, 2, 32, 323223323))


def fa(x):
    temp = x
    x = x-1
    while x > 0:
        temp = temp*x
        x = x-1
    return temp


# print(fa(5))


def fa2(x):
    if(x == 1):
        return 1
    else:
        return fa2(x-1)*x


# print(fa2(5))

# print(type(i for i in range(3)))

# def my(*list):
#     if len(list)==3:
#         return (x for x in range(list[0],list[1],list[2]))

# a = [1, 2]


# def ar(v, list, low, high):
#     mid = (low+high)//2
#     if(low > high):
#         return "false"
#     if(list[mid] == v):
#         return "True"
#     elif(list[mid] < v):
#         return ar(v, list, mid+1, high)
#     else:
#         return ar(v, list, low, mid-1)


# print(ar(10, [1, 2, 3, 4, 5], 0, 4))


# def merge(a, b):
#     temp = []
#     while True:
#         if(len(a) == 0 or len(b) == 0):
#             temp.extend(a)
#             temp.extend(b)
#             return temp
#         if(a[0] > b[0]):
#             temp.append(b.pop(0))
#         else:
#             temp.append(a.pop(0))


# def merge_sort(list):
#     check = len(list)
#     if(check == 1):
#         return list
#     else:
#         a = merge_sort(list[:check//2])
#         b = merge_sort(list[check//2:])
#         return merge(b, a)


# print(merge_sort([1, 3, 478, 5643, 423]))
# add()
# a = 1
# temp = 0
# while a != 0:
#     a = int(input())
#     temp += a
# print(temp)


# def fa():
#     return add


# print(fa()(1, 2))


a = int(input())
set = [int(input()) for x in range(a)]
temp = [0]*max(set)
temp[0] = [1, 0]
temp[1] = [0, 1]
for x in range(2, a):
    a = temp[x-1][0]+temp[x-2][0]
    b = temp[x-1][1]+temp[x-2][1]
    temp[x] = [a, b]
for x in set:
    print(temp[x][0], temp[x][1])
