'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''

# efficient approach : double binary search : Time Complexity : O(log n) + O(log m) = O(log n +log m)

def searchMatrix(matrix, target):
    rows , cols = len(matrix), len(matrix[0])
    top, bot = 0, rows - 1

    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1           #shift down
        elif target < matrix[row][0]:
            bot = row - 1          # shift up
        else:
            break
    
    # no val found
    if not (top <= bot):
        return False
    
    # search on current row
    row = (top + bot) // 2
    l , r = 0 , cols -1
    while l <= r:
        m = (l + r) // 2

        if target > matrix[row][m]:   #if target is greater search in right side
           l =  m + 1
        elif target < matrix[row][m]: # shift right pointer to left
            r = m - 1
        else:
            return True
    return False












# naive approach
# def searchMatrix(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == target:
#                 return True
#             return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 0
print(searchMatrix(matrix, target))