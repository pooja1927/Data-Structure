queue=[]
def enqueue():
    if len(queue)==n:
        print('queue is full')
    else:
        a=int(input('enter a number'))
        queue.append(a)
def dequeue():
    if len(queue)==0:
        print('queue is empty')
    else:
        queue.pop(0)

def display():
    print(queue)

n=int(input('enter the size of queue'))
while True:
    x=int(input('enter the operations(1.enqueue,2.dequeue,3.display,4.exit)'))
    if x==1:
        enqueue()
    elif x==2:
        dequeue()
    elif x==3:
        display()
    elif x==4:
        break
    else:
        print('enter a valid operation')