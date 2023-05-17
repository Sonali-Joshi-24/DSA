'''
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''

def merge(nums1 ,m, nums2, n):
    # last index nums1
    last = m + n - 1

    # merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1

    # fill nums 1 with all leftover ele of nums2
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
        

    
nums1 = [1, 2, 3, 0, 0, 0]  # Initial nums1 list with extra space
m = 3  # Number of elements in nums1
nums2 = [2, 5, 6]  # nums2 list
n = 3  # Number of elements in nums2

merge(nums1, m, nums2, n)
print(nums1)