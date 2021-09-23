# def say_hello(i=10):
#     print(i)
#     i=i-1
#     if(i>0):
#         say_hello(i)
# say_hello()

# def big(a,b):
#     print(a)if a-b>0 else print(b)

# big(3,2)

# def add(first,second):
#     print(first,second)
# add(first='32',second="dfd")

# def hello(age,name='user'):
#     print(age,name)
# hello(1)

# def print_tp(**t):
#     # t1=list(t)
#     print(t['first'])
# print_tp(first=1,two=2,three=3,four=4)

# def sum_int(*t):
#     sum=0
#     for x in t:
#         if type(x) is int or type(x) is float:
#          sum+=x 
#     print(sum)
# sum_int(1,1,1.0,'1',True)

# def func(first,second):
#     print(first,second)

# params=[1,2]
# params2=(1,2)
# params3={'first':1,'second':2}

# func(**params3)

# def int_func():
#     return 1
# def float_func():
#     return 1.1
# def list_func():
#     return [1,2,3]
# def set_func():
#     return {1,2,3}
# def tuple_func():
#     return 1,2,3
# def dic_func():
#     return {1:1,2:2}
# def str_func():
#     return 'hi'
# def if_func():
#     return True
# print(if_func(),type(if_func()))

# *t 로 받을 경우 2차원 배열로 받음
# def func(t):
#     y=min(t)
#     return y

# a=[1,2,3]
# print(min(a))
# print(func(a))

# def info(arr):
#    return sum(arr),sum(arr)/len(arr)
# sum,avg=info((1,2,3,4))
# print(sum,avg)


# def func(t):
#     return min(t),max(t)

# max,min=func([i for i in range(1,10)])
# print(max,min)

# def func2(t):
#     return {'arr':min(t),'arr2':max(t)}

# max=func([i for i in range(1,10)])
# print(max)


# sum=0
# def total(values):
#     sum=0
#     for i in values:
#         sum+=i
#     print(sum)
# total([1,2,3])
# print(sum)


# print(sum)
# def total(values):
#     global sum
#     sum=0
#     for i in values:
#         sum+=i
#     print(sum)
# total([1,2,3])
# print(sum)

# def count_down(n):
#     if n==0:
#         return
#     print(n)
#     count_down(n-1)
# count_down(1001)

# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)

# def factorial2(n):
#     sum=1
#     for i in range(1,n+1):
#         sum=sum*i
#     return sum

# print(factorial2(5))

# def my_generator():
#     print('1 반환')
#     yield 1
#     print('2 반환')
#     yield 2
#     print('3 반환')
#     yield 3
# list=[i for i in my_generator()]
# # print(list)
# gen=my_generator()
# print(next(gen))

# def my_range(*arr):
#     start=0
#     step=1
#     end=0
#     if len(arr)==1:
#         end=arr[0]
#     elif len(arr)==2:
#         start=arr[0]
#         end=arr[1]
#     else :
#          start=arr[0]
#          end=arr[1]
#          step=arr[2]
#     while start<end:
#         yield start
#         start+=step

# a=[i for i in my_range(5)]
# print(a)
# for i in range(5):
#     print(i)
# for i in my_range(1,10,2):
#     print(i)

# 고차 함수
# def add(first,second):
#     return first+second
# def sub(first,second):
#     return first-second

# def executor(func,op,params,param2):
#     return func[op](params,param2)

# func={'+':add,'-':sub}
# print(executor(func,'-',1,2))

# 함수리턴 함수
# nums=4334
# def calculate(op):
#     nums=334343
#     def add(num1,num2):
#         global nums
#         return num1+num2+nums
#     def sub(num1,num2):
#         return num1-num2
#     if op=='+':
#         return add
#     else: 
#         return sub
# print(calculate('+')(1,2))

# def func():
#     value=2
#     def nested_func():
#         # 값을 덮어쓸때
#         nonlocal value
#         value=3
#         print('nested',value)
#     nested_func()
#     print('outer',value)
# func()

# 함수를 다시 정의 하면 덮어 써짐 주의
# 그래서 라이브러리 쓸때는 라이브러리 이름.메서드
# 이렇게씀
# print(min([1,2,3,4]))
# def min(arr):
#     print(arr)
# min([1,2,3,4])


# 에러= 문법적인오류
# 오류=런타임할때 오류

def test():
    try:
        num=int(input())
    except Exception:
        test()
    finally:
        print(num)
test()