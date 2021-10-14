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

temp = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        ['*', 0, '#']]
print(temp.index(3))
