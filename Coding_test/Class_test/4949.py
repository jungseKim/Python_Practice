a=input()

while a!='.':
    arr=[]
    check=True
    for x in a:
        if(len(arr)==0 and (x==']' or x==')' )):
            print('no') 
            check=False
            break
        if(x=='[' or x=='('):
            arr.append(x)
        if(x==']'):
            if(arr[-1]=='['):
                arr.pop(-1)
            else:
                print('no') 
                check=False
                break
        if(x==')'):
            if(arr[-1]=='('):
                arr.pop(-1)
            else:
                print('no') 
                check=False
                break
    if(check):
        if(len(arr)):
            print('no')
        else:
            print('yes')
    a=input()