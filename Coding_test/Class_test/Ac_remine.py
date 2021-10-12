# import re
# T = int(input())

# P = []
# N = []
# R = []
# for _ in range(T):
#     P.append(input())
#     N.append(int(input()))
#     R.append(list(map(int, re.findall(r'\d+', input()))))

# for x in range()


# print(R)

def mom():
    a = 2

    def son(b):
        return a+b
    return son


s = mom()
s2 = mom()
print(s())
