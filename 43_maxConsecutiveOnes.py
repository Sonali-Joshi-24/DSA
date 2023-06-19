'''
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
'''

# Time complexity: O(N) and Space : O(1)

def findMaxConsecutiveOnes(nums):
    maximum = 0
    curr_no_of_ones = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            curr_no_of_ones += 1
            maximum = max(curr_no_of_ones, maximum)
        else:
            curr_no_of_ones = 0

    return maximum




