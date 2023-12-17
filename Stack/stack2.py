stack=[]
def push_no():
    if len(stack)==n:
        print('stack is full')
    else:
        b=int(input('enter element you want to push'))
        stack.append(b)
        
def pop_no():
    if len(stack)==0:
        print('stack is empty')
    else:
        stack.pop()

def display():
    print(stack)
  

n=int(input('enter the size of stack'))
while True:
    a=int(input('enter the oprations you want(1.push,2.pop,3.display,4.exit)'))
    if a==1:
        push_no()
    elif a==2:
        pop_no()
    elif a==3:
        display()
    elif a==4:
        break
    else:
        print('enter a valid operation')