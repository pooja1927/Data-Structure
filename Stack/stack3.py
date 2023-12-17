stack=[]

def pop_no():
    if len(stack)==0:
        print('stack is empty')
    else:
        stack.pop()
        print(stack)
       

def push_no():
    if len(stack)==n:
        print('stack is full:')
    else:
        a=int(input('enter the element:'))
        stack.append(a)
        print(stack)
      
#def display():
 #   print(stack)
    
n=int(input('enter the size of stack:'))

while True:
        x=int(input('enter the operation:(1.push,2.pop,3.display,4.exit)'))
        if x==1:
            push_no()
        elif x==2:
            pop_no()
        #elif x==3:
         #   display()
        elif x==4:
            break
        else:
            print('enter a valid operation')
