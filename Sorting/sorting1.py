# lst=[3,2,23,2,12,14]
# for i in range(len(lst)):
#     small=lst[i]
#     for j in range(i+1,len(lst)):
#         if small>lst[j]:
#             small=lst[j]
#     small_index=lst.index(small,i)
#     lst[i],lst[small_index]= lst[small_index],lst[i]
# print(lst)


#bubble sort
# lst=[3,2,23,12,14]
# for i in range (len(lst)-1):
#     for j in range(len(lst)-1):
#         first=lst[i]
#         next=lst[i+1]
#         if first>next:
#             lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst) 


#quick sort

# lst=[2,6,12,8,9,10]
# for i in range(len(lst)):
#     left=0
#     right=len(lst)-2
#     pivot=len(lst)-1
#     for j in range(len(lst)):
#         if left<=right:
#             if lst[left]<=lst[pivot]:
#                 left=left+1
#             else:
#                 if lst[right]>=lst[pivot]:
#                     right=right-1
#                 else:
#                     lst[left],lst[right]=lst[right],lst[left]
#         else:
#             lst[pivot],lst[left]=lst[left],lst[pivot]
# print(lst)


#linear searrch

lst= [2,3,5,4,3,8,9]
key=int(input('enter the key:'))
lst1=[]

def linear_search(lst,key):
    for i in range (len(lst)):
        if lst[i]==key:
            lst1.append(i)

    if len(lst)>0:
        print('key is found in following locations')
        print(lst1)
    else:
        print('key is not found')
linear_search(lst,key)

    
