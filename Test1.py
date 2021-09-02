# print("\    /\\")
# print(" )  ( ')")
# print('(  /  )')
# print(' \(__)|')

# a,b=map(int,input().split())
# print(a+b)

# A=7
# B=3
# A,B=map(int,input().split())
# print(A+B)
# print(A-B)
# print(A*B)
# print(int(A/B))
# print(A%B)

A,B,C=map(int,input().split())
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)