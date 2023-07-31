class Solution:
    def subsetWithoutDuplicates(self, nums):
        res = []
        nums.sort()

        def backtrack(index, subset):
            # base case
            if index == len(nums):
                res.append(subset[::])   #making copy of subset using [::]
                return 
            
            # All subsets that include nums[i] (the num we are at)
            subset.append(nums[index])
            backtrack(index + 1, subset)
            subset.pop()

            # All subsets that do not include nums[i] (duplicates)
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, subset)

        backtrack(0, [])
        return res

ans = Solution()
print(ans.subsetWithoutDuplicates([1,2,2]))
    


        

    