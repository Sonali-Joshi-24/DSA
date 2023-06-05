'''
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check if its the start of sequence
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))



















# nums = [100,4,200,1,3,2]
# numSet = set(nums)
# for n in nums:
#     # print(n)  100, 4,200,1,3,2



