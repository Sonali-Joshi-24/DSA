'''
nums = [-1,0,1,2,-1,-4]
output = [[-1,-1,2], [-1,0,1]]

'''




# 1. loop through array and find out the triplets
# 2. insert that triplets in an array
# 3. put that triplets arr in a arr


'''
sort the input arr
Time: O(nlogn) + o(n^2) = O(n^2)
Space : O(N)
''' 
# def threeSum(nums):
#     res = []
#     nums.sort()

#     # use each number in input arr as a possible 1st value
#     for i , a in enumerate(nums):
#         if i > 0 and a == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             threeSum = a + nums[l] + nums[r]
#             if threeSum > 0:
#                 r -= 1
#             elif threeSum < 0:
#                 l += 1
#             else:
#                 res.append([a, nums[l], nums[r]])
#                 l += 1
#                 while nums[l] == nums[l - 1] and l < r:
#                     l += 1
#     return res
# nums = [-1,0,1,2,-1,-4]
# print(threeSum(nums))



# num1 = [-1,0,1,2,-1,-4]
# num1.sort()
# print(num1)

# for index, value in enumerate(num1):
#     print(index,value)



