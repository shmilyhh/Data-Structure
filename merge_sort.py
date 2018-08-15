def sortIntegers(A):
    temp = [i for i in A]
    mergeSort(0, len(A) - 1, A, temp)

def mergeSort(start, end, A, temp):
    if start >= end:
        return
    
    mid = start + (end - start) // 2
    mergeSort(start, mid, A, temp)
    mergeSort(mid+1, end, A, temp)
    merge(start, mid, end, A, temp)

def merge(start, mid, end, A, temp):
    left, right = start, mid + 1
    index = start

    while left <= mid and right <= end:
        if A[left] < A[right]:
            temp[index] = A[left]
            left += 1
        else:
            temp[index] = A[right]
            right += 1
        
        index += 1

    while left <= mid:
        temp[index] = A[left]
        left += 1
        index += 1
    
    while right <= end:
        temp[index] = A[right]
        right += 1
        index += 1

    for i in range(start, end + 1):
        A[i] = temp[i]

    
temp = [2,1,3,6,4]
sortIntegers(temp)
print(temp)