# def linearSearch(lst, key):
#     for i in range(len(lst)):
#         if lst[i]==key:
#             print(f'key is found in {i} position')
#             break
#     else:
#         print('key is not found')

def linearSearch(lst, key):
    lst1 = []
    for i in range(len(lst)):
        if lst[i]==key:
            lst1.append(i)

    if len(lst1)>0:
        print('Key is found at following locations')
        print(lst1)
    else:
        print('Key is not found')


lst=[10,15,17,3,20,22,23,3]
key=int(input('enter key: '))
linearSearch(lst, key)