import user

# 이거는 되는데
# from user import _merge
# 이거는 안됨 
# from user import *

print(user.hello())
print(user.defaultUser.hello())
# 이렇게 하면 무조건 클래스가 선택
myUser=user.User()
print(myUser.hello())

print(user._merge('a','b'))