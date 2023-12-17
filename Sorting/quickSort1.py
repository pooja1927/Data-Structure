def pivot_place(lst, first, last):
    pivot = lst[first]
    left = first+1
    right = last
    while True:
        while left<=right and lst[left]<=pivot:
            left = left+1
        while left<=right and lst[right]>=pivot:
            right = right-1
        if left>right:
            break
        else:
            lst[left], lst[right] = lst[right], lst[left]
    lst[first], lst[right] = lst[right], lst[first]
    return right


def quickSort(lst, first, last):
    if first<=last:
        pivot = pivot_place(lst, first, last)
        quickSort(lst, first, pivot-1)
        quickSort(lst, pivot+1, last)

lst = [10,4,25,3,5]
first = 0
last = len(lst)-1
quickSort(lst, first, last)
print(lst)