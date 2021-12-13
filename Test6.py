# # def merge_sort(list):
# #     if len(list) == 1:
# #         return list
# #     else:
# #         a = merge_sort(list[len(list)//2:])
# #         b = merge_sort(list[:len(list)//2])
# #     return merge(a, b)


# # def merge(list1, list2):
# #     print(list1, list2)
# #     result = []
# #     while True:
# #         if list1[0] > list2[0]:
# #             result.append(list2.pop(0))
# #         else:
# #             result.append(list1.pop(0))
# #         if len(list1) == 0 or len(list2) == 0:
# #             result.extend(list1)
# #             result.extend(list2)
# #             return result


# # print(merge_sort([1, 3, 4, 12, 2, 1, 3, 4, 12, 2]))
# # # print([1, 3, 4, 12, 2].pop())

# # class Student:
# #     def __init__(self) -> None:
# #         pass

# #     def say_hello(self):
# #         print('heelow')

# #     @classmethod
# #     def hi(cls):
# #        #  print('heelow')
# #         return cls()

# # a=Student.hi()

# # Student.hi()
# # Student.say_hello()
# # Student.say_hello()

# class User:
#     default = 'sex'

#     def __init__(self, name="user"):
#         self.name = name

#     def __repr__(self):
#         return self.default


# class Admin(User):
#     def __init__(self, name):
#         super().__init__(name)

#     def __repr__(self):
#         re super().__repr__()+self.name


# print(Admin('sexy'))

class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.rigth = right
        self.data = data


node1 = Node(8)
node2 = Node(9)
node3 = Node(4, node1, node2)
node4 = Node(5)
node5 = Node(2, node3, node4)
node6 = Node(1)
node7 = Node(6)
node8 = Node(7)
node9 = Node(3, node7, node8)
