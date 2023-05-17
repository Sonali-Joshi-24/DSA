'''
Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4 where A is repeating and B is missing
Time complexity : O(N) and Space : O(1)
'''

def repeatAndMissing(nums):
    a, b = 0, 0
    # repeating element
    for i in range(len(nums)):
        if nums[abs(nums[i]) - 1] < 0:        #if ele is already negative means missing
            a = abs(nums[i])
        else:                                # else make the ele negative
            nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

    # missing element
    for i in range(len(nums)):                     
        if nums[i] > 0:                      # if ele is positive means it is missing ele
            b = i + 1                        # since 0 based indexing return ind + 1 
            break
    return a,b

nums = [3,1,2,5,3]
print(repeatAndMissing(nums))










'''
print("nums[i-1]", nums[i] - 1)
print("nums[i]",nums[i])
print(nums[abs(nums[i] - 1)])

output :
nums[i-1] 2
nums[i] 3
2
'''