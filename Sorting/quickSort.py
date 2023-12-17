lst = [5,15,3,12,17,0]

for i in range(len(lst)):
    left = 0
    right = len(lst)-2
    pivot = len(lst)-1
    for j in range(len(lst)):
        if left<=right:
            if lst[left]<=lst[pivot]:
                left = left+1
            else:
                if lst[right]>=lst[pivot]:
                    right = right-1
                else:
                    lst[left], lst[right]=lst[right],lst[left]
        else:
            lst[left], lst[pivot] = lst[pivot], lst[left]
print(lst)