'''
A pair is said to be an inversion only when 
2 conditions :
                - arr[i] > arr[j]
                - i < j (where i and j are the index)

                eg: input : [3,2,1]
                output : 3     || (3,2), (2,1), (3,1)
'''

# effiecient approach : O(nlogn) TC --> merge sort and O(N) space
def mergeSort(arr, n):
    # temp arr to store sorted arrat in merge function
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0 ,n-1)

def _mergeSort(arr, temp_arr, left, right):
    # store inversion count
    inv_count = 0

    # make recursive call if we have more than 1 ele
    if left < right:
        mid = (left + right) // 2

        # cal inv_count in left-subarray
        inv_count += _mergeSort(arr, temp_arr, left, mid)

        # cal inv_count in right-subarray
        inv_count += _mergeSort(arr, temp_arr, mid+1, right)

        # merge 2 subarr in a sorted subarray
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count

# merge 2 sub-arr in a sorted subarray
def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0

    while i <= mid and j <= right:
        # there will be no inversion if arr[i] <= arr[j]
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # inversion will occur
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1

    # copy the remaining elements of left sub arr into temp arr
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # copy the sorted subarr into original arr
    for x in range(left, right + 1):
        arr[x] = temp_arr[x]
    return inv_count 



arr = [2,5,1,3,4]
n = len(arr)
print(mergeSort(arr, n))







# naive approach : Time Complexity : O(N^2) and Space Complexity: O(1)
# def countInversions(arr):
#     count = 0
#     for i in range(len(arr)):
#         for j in range(1, len(arr)):
#             if arr[i] > arr[j] and i < j:
#                 count += 1
#     return count
arr = [2,5,1,3,4]
# print(countInversions(arr))