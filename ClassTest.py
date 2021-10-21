# class Student():
#     a=10
#     def __init__(self,cn=20):
#         self.a=20
#         self.jo=cn
#     def say(self):
#         print('hi')
#     @classmethod
#     def create(cls,name):
#         return cls(name)
#         # 다른 객체들 삽입할때 


# ac=Student(cn=40)
# ab=Student(cn=40)
# Student.say(ab)
# # 클래스에 객체 넘겨서 실행 self 가 아규먼트

# ad=Student.create('aaa')
# ad.say()

# print(dir())

# class Circle:
#     ko=3
#     def __init__(s,x=0,y=0,r=1):
#         s.x=x
#         s.y=y
#         s.r=r
#     def __del__(s):
#         print('삭제')
#     def __repr__(s):
#         return 'ddd'
#     def __add__(s,other):
#         return s.x+other.x,s.y+other.y
#     def __sub__(s,other):
#         return s.x-other.x,s.y-other.y
# c1=Circle()
# c2=Circle(0,0,2)
# c1.ko=2

# print(id(c1.ko))
# print(id(c2.ko))


# print(dir())

# print(dir('dd'))
# del c2
# print('sssss')
# print(c1)

# print(c1+c2)

# class User:
#     def __init__(self,name="user"):
#         self.name=name
#         self.address=''
#         self.email=''
#         self.phone=''
#     def __repr__(self):
#         return self.name
# user1=User(name="hi")
# user2=User()
# print(user1)
# print(user2)

class Member:
    def __init__(self):
        self.id="0"
    def __repr__(self):
        return self.id
class St(Member):
    def __init__(self):
        super().__init__()
        self.c='a'
    def __repr__(self):
        return super().__repr__()+'aa'
    

s=St()
print(s)
# 메소드는 사용가능 그냥 변수만 사용못하는것일듯
