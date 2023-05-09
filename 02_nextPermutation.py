# arr = [1,2,3]
# permutation : [1,2,3], [1,3,2] , [2,1,3], [2,3,1], [3,1,2], [3,2,1]

# input : nums = [1,2,3]
# output : nums = [1,3,2]

'''
1,3|,5,4,2
3 is the number that is going to change now how do we get to know
with what number is it going to change (it will change with next possible number of 3 i.e. 4)

TC : O(N) [index 1 find] + O(N) [index2 find] + O(N) [reverse]  = O(3n) = O(N)
SC : O(1)
'''




def nextPermutation(nums):
    length = len(nums)
    # base case
    if length <= 2:
        return nums.reverse()
    
    pointer = length - 2   #pointer at 2nd last element

    while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:   #keep moving the pointer until we are in desending pattern 
        pointer -= 1
    
    # if the sequence is like 5,4,3,2,1
    if pointer == -1:
        return nums.reverse()
    
    for x in range(length - 1, pointer, -1):
        if nums[pointer] < nums[x]:
            nums[pointer], nums[x] = nums[x] , nums[pointer]
            break

    nums[pointer + 1 :] = reversed(nums[pointer + 1 :])
    return nums


nums = [1,2,3]
print(nextPermutation(nums))










