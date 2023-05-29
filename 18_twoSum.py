def twoSum(nums, target):
    seen = {}
    for i , n in enumerate(nums):
        remaining = target - n
        if remaining in seen:
            return [seen[remaining], i]
        seen[n] = i
nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))