# # # import os

# # # print(os.name)
# # # print(os.getcwd())

# # # str = 'heelow my name'
# # # list = list(str)
# # # str = 'dd'.join(list)
# # # print(str)


# # list = [0]*10
# # top = 0


# # def push(list, value):
# #     global top
# #     if top > 9:
# #         return print('stack overflow')
# #     top += 1
# #     list[top] = value


# # def pop(list):
# #     global top
# #     if top <= 0:
# #         return print('stack empty')
# #     top -= 1
# #     del list[top]


# # push(list, 1)

# # import statistics as st


# class Ad:
#     sex = 'xd'

#     def __init__(self):
#         pass

#     def add(self):
#         print('dfdfd')

#     @classmethod
#     def dd(cls):
#         print('hellpw')


# class AC(Ad):
#     def __init__(self):
#         pass


# h = AC()
# print(h.add())

# # ac = Ad()
# # ac.dd()
# # print(dir(ac))


# import os
# # print(os.name)
# # os.system('notepad')
# os = '1'
# print(os)
def binarySearch(list, value, low, high):
    if low > high:
        return print('없음')
    mid = (low+high)//2
    if list[mid] == value:
        return print('찾음')
    if list[mid] > value:
        binarySearch(list, value, low=low, high=mid-1)
    else:
        binarySearch(list, value, low=mid+1, high=high)


binarySearch([1, 2, 3, 4, 5, 9], 12, 0, 5)
