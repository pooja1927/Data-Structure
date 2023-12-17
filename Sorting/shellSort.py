def shell_sort(lst):
    gap=len(lst)//2
    while gap>0:
        for i in range(gap,len(lst)):
            current_elment=lst[i]
            pos=i
            while pos>=gap and lst[pos-gap]>current_elment:
                lst[pos]=lst[pos-gap]
                pos=pos-gap
            lst[pos]=current_elment
        gap=gap//2


lst=[34,26,93,17,77,31,44]
shell_sort(lst)
print(lst)
