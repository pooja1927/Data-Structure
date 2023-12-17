# lst=[5,15,3,12,17,0,3]
# for i in range (len(lst)):
#     small=lst[i]
#     for j in range(i+1,len(lst)):
#         if small>lst[j]:
#             small=lst[j]
#     small_index=lst.index(small,i)
#     lst[i],lst[small_index]= lst[small_index],lst[i]
# print(lst)

lst=[5,15,3,12,17,0,3]
for i in range (len(lst)):
    small=min(lst[i:])
    small_index=lst.index(small,i)
    lst[i],lst[small_index]= lst[small_index],lst[i]
print(lst)