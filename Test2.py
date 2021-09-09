# first='hellow "you"'
# sencod="hellow 'you'"
# multi1='''hewllow
# friend'''
# multi2="""hell
# firend"""
# print(first,sencod)
# print(multi1)
# print(multi2)


# str='hello my friend'
# split1=str.split()
# split2=str.split('e')
# print(split1)
# print(split2)
# print(str)

# str_list=list(str)
# print(str_list)
# print(str)

# join1=''.join(str_list)
# join2='*'.join(str_list)

# print(join1)
# print(join2)

# list=[0,1,2,3,4,5,6,7,8,9]
# print(list[::-1])
# print(list[8:3:-2])
# print(list[-2:3])
# print(list[-2:-4:-1])

# del list[:3]
# print(list)
# del list[2:5]
# print(list)

# a=input()
# temp=a[-3:]
# print(temp)

# 변수를 키로 할경우 값이 바뀌어도 
# 키값은 바뀌지 않는다
# a='seaol'
# capitals={a:'seoul','uk':'london'}
# print(capitals)
# capitals['japan']='tokyo'
# print(capitals)
# a=2
# capitals.update({'usa':'D.C','china':'beijing'})
# print(capitals)
# del capitals['usa']
# print(capitals)

# set1=set([1,2,3,4])
# set2={(1,2),2,3,'hellow'}

# set1.add(5)
# print(set1)
# set1.add(1)
# print(set1)
# set1.remove(4)
# print(set1)
# set1.update([7,8])
# print(set2-set1)
# print(set1|set2)
# print(set1&set2)

# a=10
# b=2.0

# print( False == True)

# a=int(input())

# if a>=0:
#     print("ok")
# else:
#     print("ng")

# a=input()
# if len(a)>7:
#     print('ok')
# else:
#     print('nj')

# a,b=map(int,input().split())
# if (a * b)>0:
#     print('ok')
# else :
#     print('ng') 

# a=int(input())
# if a%2==0:
#     print('even')
# else :
#     print('obb')

# a=input()
# b=len(a)
# # print(b)
# if 11>b>3:
#     print('ok')
# else :
#     print('ng')

# a,b=map(int,input().split())
# result=a+b
# print('ok' if result>=0 else 'ng')

# a,b=map(int,input().split())
# temp=input()
# print(a+b if temp=='+' else a-b)

tp=[1,2,3,4,5,6,7,8,9]
# del tp[::2]
# for t in tp:
#     print(t)
# a=0
# b=0
# def ho(t): 
#     global a
#     a+=t
# def go(t):
#     global b
#     b+=t
# for t in tp:
#    ho(t) if t%2==0 else go(t)

# print(a)
# print(b)

# for i in range(2,9):
#     print(2*i)

# for i in range(4):
#     for j in range(i+1):
#         print('*',end='')
#     print()

# 시험 문제 나옴 
# enumerate

arr1=[1,2,3,4]
arr2=[9,'5','4']
arr3=['a','b','c']
for i,j,k in zip(arr1,arr2,arr3):
    print(i,j,k)
# arr=[i for i in range(0,5,2)]
# print(arr)

# 참조한다음 값 고정되는 거같음
# a=10
# for i in range(a):
#     a+=1
#     print(i)

# 0으로 초기화할때
# list=[0]*1000

# list=[i for i in range(1,11,2)]
# print(list)
# list2=[i*3 for i in range(10)]
# print(list2)


# 방법 2개
n=int(input())
# list=[0]*n
# s=input()
# for i in range(n):
#     list[i]=s
# print(list)

# list=[s for i in range(n)]
# print(list)

n=int(input())
arr=[i for i in range(n)]
for i in range(n):
    arr[i]=int(input())
arr2=[s for s in arr if s>=0] 
print(arr2)
