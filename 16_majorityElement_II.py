'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:

Input: nums = [3,2,3]
Output: [3]

Rules:
1. since we are looking for 2 majority element there r going to be 2 cadidate 
2. if the current_ele == either can1 or cand2 only that particular cand value will increase n other one will remain as it is

'''

def majorityElement(nums):
    if not nums:
        return []
    
    cand1, count1 = None, 0
    cand2, count2 = None, 0

    for num in nums:
        if cand1 == num:
            count1 += 1
        
        elif cand2 == num:
            count2 += 1

        elif count1 == 0:
            cand1 = num
            count1 += 1

        elif count2 == 0:
            cand2 = num
            count2 += 1

        else:
            count1, count2 = count1 - 1, count2 - 1
        
    return [x for x in (cand1, cand2)  if nums.count(x) > len(nums) // 3]
        
nums = [3,2,3]
print(majorityElement(nums))

