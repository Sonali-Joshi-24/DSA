# input : nums [2,0,2,1,1,0]
# output : nums [0,0,1,1,2,2]
# Time complexity : O(N) and Space Complexity : O(1)


'''
- we will initialize low , mid at 0 and high pointer at len(nums) - 1
- the low and mid will point at 0 index and the high will point to last ele
- while mid < high
- conditions to check:
    - if nums[mid] == 0 then swap nums[low], nums[mid], mid ++ low ++
    - if nums[mid] == 1 then mid ++
    - if nums[mid] == 2 the swap nums[mid], nums[high], high --
 
'''


def sortColor(nums):
    low , mid = 0,0
    high = len(nums) - 1

    while mid < high:
        if nums[mid] == 0:
            nums[low] , nums[mid] = nums[mid], nums[low]
            mid += 1
            low += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums

nums = [2,0,2,1,1,0]

print(sortColor(nums))

