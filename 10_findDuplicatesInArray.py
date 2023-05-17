'''
input : nums = [1,3,4,2,2]
output : 2
explanation : since 2 is repeating number in array

'''
# navie approach 
# def findDuplicates(nums):
#     nums.sort()
#     for i in range(len(nums)):
#         if nums[i] == nums[i + 1]:
#             return nums[i]

# floyd loop detection algorithm
# Time : O(n) and Space : O(1)
def findDuplicates(nums):
    fast = 0
    slow = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if fast == slow:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow


nums = [3,1,3,4,2]
print(findDuplicates(nums))
    