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

# A,B,C=map(int,input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

num=int(input())
for i in range(num):
    strs=''
    if i<num/2:
        for j in range(i+1):
            strs+=str(j)
    else :
        for j in range(num-i):
            strs+=str(j)
    print(strs)