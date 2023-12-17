def insertion_sort(lst):
    for i in range(1,len(lst)):
        current_element=lst[i]
        pos=i
        while current_element>lst[pos-1] and pos>0:
            lst[pos]=lst[pos-1]
            pos=pos-1
        lst[pos]=current_element

lst=[10,4,25,3,5]
insertion_sort(lst)
print(lst)