'''
# Sliding Window
Input : s = "abcabcbb"
Output : 3
Explanation : The answer is "abc", with the length of 3.

Time Complexity : O(N) || MEmory : O(N) due to set
'''

# def lengthOfLongestSubstring(s):
#     charSet = set()
#     left = 0
#     result = 0

#     for r in range(len(s)):
#         while s[r] in charSet:  #duplicate
#             charSet.remove(s[left])
#             left += 1
#         charSet.add(s[r])                 # no duplicate add to set
#         result = max(result, r - left + 1)
#     return result



# string = "abcabcbb"
# print(lengthOfLongestSubstring(string))


def lengthOfLongestSubString(s):
    dict = {}
    result = 0
    i = 0        #starting index

    for j, value in enumerate(s):
        # check if duplicate
        if value in dict:
            # update i pointer to move forward (to right)
            i = max(i, dict[value] + 1)
        # update the result 
        result = max(result, (j - i + 1))
        # update the j for duplicate val
        dict[value] = j
    return result

string = "abcabcbb"
print(lengthOfLongestSubString(string))




