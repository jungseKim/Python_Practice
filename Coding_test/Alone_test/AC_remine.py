import re

T=int(input())
P=[]
N=[]
R=[]
check=1
for _ in range(T):
    P.append(input())
    N.append(int(input()))
    R.append(list(map(int,re.findall(r'\d+',input()))))

print(R)
for i in range(T):
    if(N[i]!=len(R[i])):
        print('aaaaaaaa')
        N[i]='error'
    else:
        try:
            for index,y in enumerate(P[i]):
                if(y=='R'):
                    check=check*-1
                else:
                    if(check>0):
                        R[i].get()
                    else:
                        R[i].pop()
            if(check<0):
                R[i].reverse()
            R[i]=','.join(map(str,R[i]))
            chekc=1    
        except :
             R[i]='error'
             chekc=1
for x in R:
    if('error'==x):
        print(x)
    else:
        print('['+x+']')