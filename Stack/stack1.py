stack=[]
def pop_no():
    if len(stack)==0:
        print('stack is empty')
    else:
        a=stack.pop()
        print(f'{a} is removed from stack' )
        print(stack)

def push_no():
    b=int(input('enter element you want to push'))
    stack.append(b)
    print(stack)

while True:
    x=int(input('enter the operation number(1.push,2.pop,3.exit)'))
    if x ==1:
        push_no()
    elif x==2:
        pop_no()
    elif x==3:
        break
    else:
        print('enter valid operation number')
    