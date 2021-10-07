import sys
a=int(sys.stdin.readline().rstrip())
for i in range(a):
    fx=[x for x in sys.stdin.readline().rstrip()]
    length=int(sys.stdin.readline().rstrip())
    arr=sys.stdin.readline().rstrip()
    if(len(arr)>2):
        arr2=[int(x) for x in arr[1:-1].split(',')]
    else:
        arr2=[]
    a=2
    if(length!=len(arr2)):
        print('error')
        continue
    start=1
    a=2
    for index,x in enumerate(fx):
        if('R'==x):
            start=start*-1
        else:
            if(len(arr2)==0):
                a=1
                print('error')
                break
            else:
                if(start==1):
                    arr2.pop(0)
                else:
                    arr2.pop(-1)   
    if(start==-1):
            arr2.reverse()
            # 이거 하지말고 for 바로 문에서 해보자    
    if(a==2):
        if(len(arr2)==0):
             print('[]')
             continue
        print('[',end='')
        for index,x in enumerate(arr2):
            if(index!=len(arr2)-1):
                print(x, end='')
                print(',',end='')
            else:
                print(x,end='')
                print(']')