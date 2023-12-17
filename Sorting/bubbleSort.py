# lst=[5,15,3,12,17,0]
# for j in range(len(lst)-1):
#     for i in range(len(lst)-1):
#         first=lst[i]
#         next=lst[i+1]
#         if first>next:
#             lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst)

lst=[5,15,3,12,17,0]
for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        first=lst[i]
        next=lst[i+1]
        if first<next:
            lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)