from linklist import Linkedlist

s = Linkedlist()
a = [1,2,2,1]
[s.insert(i) for i in a]
s.traverse_ll()

# Efficient Approach: Two Pointer (fast and Slow)
# Time : O(N) and Space: O(1)
def isPalindrome(s):
    fast = s.getHead()
    slow = s.getHead()

    # find middle (slow pointer)
    while fast and fast.nextNode:
        fast = fast.nextNode.nextNode
        slow = slow.nextNode

    # reverse 2nd half of list
    prev = None
    while slow:
        temp = slow.nextNode
        slow.nextNode = prev
        prev = slow
        slow = temp
    
    # check if it is palindrome
    left , right = s.getHead(), prev

    while right:
        if left.data != right.data:
            return False
        left = left.nextNode
        right = right.nextNode
    return True

print(isPalindrome(s))








'''

# O(N) time and O(N) memory(since using array)
# array solution convert linklist to arr and solve the palindrome problem
def isPalindrome(s):
    nums = []

    h = s.getHead()
    while h:
        nums.append(h.data)
        h = h.nextNode

    # palindrome for arr
    l, r = 0, len(nums) - 1
    while l <= r:
        if nums[l] != nums[r]:
            return False
        l += 1
        r -= 1
    return True

print(isPalindrome(s))
'''