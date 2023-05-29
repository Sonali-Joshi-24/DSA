'''
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''
# Time Complexity: O(N * m) and Space : O(n) for row

def uniquePaths(m, n):
    # making bottom row all 1
    row = [1] * n
    
    # iterate thro
    for i in range(m - 1):
        newRow = [1] * n
        for j in range(n - 2, -1 , -1):  #go from right to left leave the last row
            newRow[j] = newRow[j + 1] + row[j]
        row = newRow
    return row[0]
