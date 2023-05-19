'''
The majority element is the element that appears more than ⌊n / 2⌋ times. 

Input: nums = [3,2,3]
Output: 3

'''
# Solution 1 : using hashmap : TC: O(N) but SC: O(N)
# def majorityElement(nums):
#     count = {}
#     res , maxCount = 0 , 0
    
#     for n in nums:
#         count[n] = 1 + count.get(n, 0)
#         res = n if count[n] > maxCount else res
#         maxCount = max(count[n], maxCount)
#     return  res


# Solution 2: getting rid of hash-map Algorithm : boyer-more algorith
'''
[1,2,2,3,3,1,1]
1 - 3  ...max
2 - 2
3 - 2
'''
# Time :O(n) and Space : O(1)
def majorityElement(nums):
    res , count = 0, 0

    for n in nums:
        if count == 0:
            res = n
        count += (1 if n == res else -1)
    return res







