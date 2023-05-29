
'''
Time Complexity: O(n^3), where n is the length of the input array nums. The two outer loops iterate over all possible pairs, and the inner while loop takes O(n) time in the worst case. The sorting operation at the beginning takes O(n log n) time, but it is dominated by the overall cubic complexity.

The space complexity also remains the same:

Space Complexity: O(1), as the additional space used is only for storing the results list, which grows based on the number of valid quadruplets found. It does not depend on the size of the input array.

The fourSum function does not use any additional data structures that scale with the input size, so the space complexity is constant or O(1).
'''

def fourSum(nums,target):
    nums.sort()     #sort the input array
    result = []     #store the quadraplets

    for i in range(len(nums) - 3): 
        if i > 0 and nums[i] == nums[i - 1]:
            continue    #skip the duplicate for first number

        for j in range(i + 1, len(nums) - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue     #skip the duplicate for second number

            # 2 pointer approach for rest numbers
            left = j + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1      # skip duplicate for 3rd element
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1     #skip the duplicate for 4th element

                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
    return result

# nums = [1,0,-1,0,-2,2]
# target = 0
nums = [1,0,-1,0,-2,2]
target = 0

print(fourSum(nums,target))