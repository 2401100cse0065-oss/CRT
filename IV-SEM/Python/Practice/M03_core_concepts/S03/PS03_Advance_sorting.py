
#Quick sort
def partition (arr,low, high):
    pivot = arr[low]
    i,j = low + 1, high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    arr[low],arr[j] = arr[j],arr[low]
    return j    

print(partition([54,26,93,17,77,31,44,55,20],0,8))


def quicksort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)            
    return arr  
print(quicksort([54,26,93,17,77,31,44,55,20],0,8))  
  