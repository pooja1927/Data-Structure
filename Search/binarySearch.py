def binarySearch(lst, key):
    lst.sort()
    start = 0
    end=len(lst)-1
    found = False
    while start<=end and found==False:
        mid = (start+end)//2
        if key==lst[mid]:
            print(f'Key is found at index {mid}')
            found = True
        elif key>lst[mid]:
            start = mid+1
        else:
            end = mid-1
    
lst = [10, 15, 8, 9, 13, 4, 2]
key = int(input('Enter the key: '))
binarySearch(lst, key)