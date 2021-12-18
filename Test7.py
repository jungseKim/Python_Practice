# # # # # import os

# # # # # print(os.name)
# # # # # print(os.getcwd())

# # # # # str = 'heelow my name'
# # # # # list = list(str)
# # # # # str = 'dd'.join(list)
# # # # # print(str)


# # # # list = [0]*10
# # # # top = 0


# # # # def push(list, value):
# # # #     global top
# # # #     if top > 9:
# # # #         return print('stack overflow')
# # # #     top += 1
# # # #     list[top] = value


# # # # def pop(list):
# # # #     global top
# # # #     if top <= 0:
# # # #         return print('stack empty')
# # # #     top -= 1
# # # #     del list[top]


# # # # push(list, 1)

# # # # import statistics as st


# # # class Ad:
# # #     sex = 'xd'

# # #     def __init__(self):
# # #         pass

# # #     def add(self):
# # #         print('dfdfd')

# # #     @classmethod
# # #     def dd(cls):
# # #         print('hellpw')


# # # class AC(Ad):
# # #     def __init__(self):
# # #         pass


# # # h = AC()
# # # print(h.add())

# # # # ac = Ad()
# # # # ac.dd()
# # # # print(dir(ac))


# # # import os
# # # # print(os.name)
# # # # os.system('notepad')
# # # os = '1'
# # # print(os)
# # # def binarySearch(list, value, low, high):
# # #     if low > high:
# # #         return print('없음')
# # #     mid = (low+high)//2
# # #     if list[mid] == value:
# # #         return print('찾음')
# # #     if list[mid] > value:
# # #         binarySearch(list, value, low=low, high=mid-1)
# # #     else:
# # #         binarySearch(list, value, low=mid+1, high=high)


# # # binarySearch([1, 2, 3, 4, 5, 9], 12, 0, 5)


# # def binary(list, value, low, high):
# #     mid = (low+high)//2
# #     if low > high:
# #         return print('없음')
# #     if list[mid] == value:
# #         return print('찾음')
# #     if list[mid] > value:
# #         binary(list, value, low=low, high=mid-1)
# #     else:
# #         binary(list, value, low=mid+1, high=high)


# # binary([1, 2, 3, 4, 5, 6, 7, 8], 11, 0, 7)


# list = [0]*10
# top = 0


# def push(value):
#     global top
#     if top > 9:
#         return print('stack overflow')
#     list[top] = value
#     top += 1


# def pop():
#     global top
#     if top < 1:
#         return print('stack empty')
#     del list[top-1]
#     top -= 1


# push(1)
# pop()
# pop()
# print(list)

def func(**a):
    print(a)
    for i in a:
        print(i, a[i])


func(ddd=2, ddy=3)

a = {'ddd': 2, 'ddy': 3}

for i in a:
    print(i, a[i])
