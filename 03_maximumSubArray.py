# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# TC : O(N) || SC: O(1)


def maxSubArray(nums):
    currSum , maxSum = 0 , float("-inf")

    for num in nums:
        currSum += num
        maxSum = max(currSum, maxSum)

        if currSum < 0:
            currSum = 0
    return maxSum
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))