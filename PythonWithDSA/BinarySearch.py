def BinarySearch(arr,key):
    count = 0
    start = 0
    end = len(arr)-1
    mid = int((start + end) / 2)

    while(start <= end):
        if(key == arr[mid]):
            return mid
        if(key > arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
        mid = int((start + end) / 2)
    return -1
    
val = list([2,6,12,15,20,26,30])
result = BinarySearch(val, 30) 
print(result)

