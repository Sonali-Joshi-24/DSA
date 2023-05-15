'''
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

pattern :
0th row becomes last col (3rd col)
1st row become (last - 1)  last col (2nd col)
2nd row becomes last - 2 last col (1st col)

Solution
1. transpose all rows --> so they become cols
so 
transpose col                   
   1st col     = 0th row becomes last col (3rd col)
   2nd col     = 1st row become (last - 1)  last col (2nd col)
   3rd col     = 2nd row becomes (last - 2) last col (1st col)

so in order to bring it in sequence
2. swap (1st and 3rd col)
and keep 2nd as it is

'''

def rotate(matrix):
    # transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i,j]

    # swap columns
    for j in range(len(matrix)//2):
        for i in range(len(matrix)):
            # swap curr row  with last col val of same row
            matrix[i][j], matrix[i][len(matrix) - 1 - j] = matrix[i][len(matrix) - 1 - j], matrix[i][j]