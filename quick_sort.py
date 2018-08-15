import random


def quickSortHelper(alist, start, end):
    """Partition a list.

    Arguments:
        alist {list} -- a list of data
        start {int} -- the start index
        end {int} -- the start index

    Returns:
        split
    """
    if start >= end:
        return

    left = start
    right = end

    pivotvalue = alist[random.randint(0, end - start) + start]

    while left <= right:
        while left <= right and alist[left] < pivotvalue:
            left += 1

        while left <= right and alist[right] > pivotvalue:
            right -= 1

        if left <= right:
            tmp = alist[left]
            alist[left] = alist[right]
            alist[right] = tmp

            left += 1
            right -= 1

    quickSortHelper(alist, start, right)
    quickSortHelper(alist, left, end)


def quickSort(alist):
    """Quick sort.

    Arguments:
        alist {list} -- a list of data
    """
    quickSortHelper(alist, 0, len(alist)-1)


alist = [3, 6, 2, 1, 7, 8]
quickSort(alist)
print(alist)
