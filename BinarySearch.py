## Implementing Binary Search
## Author: Abhinav Dubey
## Date  : June 15, 2022

def BinarySearch(array_sorted, target):
    ''' Given a non-decreasing sorted array.
        Returns True if target is in array.
        Returns False if target is not in array.
        O(log n) time complexity. '''

    left  = 0
    right = len(array_sorted)

    while left <= right:
        mid = int((left+right)/2)
        if target < array_sorted[mid]:
            right = mid - 1
        elif target > array_sorted[mid]:
            left = mid + 1
        else:
            return True

    return False

# Test Cases
print(BinarySearch([1,2,3,4,5]  ,3))
print(BinarySearch([-3, -1, 0, 56, 128], 32))

