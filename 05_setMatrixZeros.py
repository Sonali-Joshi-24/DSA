'''
input : matrix = [[1,1,1],
                  [1,0,1],
                  [1,1,1] ]

output : matrix = [[1,0,1],
                   [0,0,0],
                   [1,0,1]  ]

we need to do this in-place

Approch : 1. In-efficient : make a copy of matrix traverse the input matrix 
                            and make changes in copy (repeated work)
                            Space Complexity : O(m*n)

          2. Bit - Efficient :instead of copy make 1 array for no. of col and 1 for row
                              mark places in arr of row and col for which we need to set to 0
                              at the end check the row and col array and set the rows and columns of
                              matrix to 0
                            Space Complexity : O(m + n)  where m and n are the 2 arr row n col
                            Time : O(m*n) 

          3. Efficient : make above 2 arr in-place 
                         Space : O(1)
                         Time : O(m*n)
'''

def setZeros(matrix):
    # O(1)
    rows , cols = len(matrix) , len(matrix[0])
    rowZeros = False

    # determine which row and col needs to be zero
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0   #make the row 0

                if r > 0:
                    matrix[r][0] = 0   #make the col 0
                else:
                    rowZeros = True
    
    # zeroing-out the main rows and columns
    for r in range(1,rows):
        for c in range(1,cols):
            # check if 1st row or 1st col is zero
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0            # set the current position we are at to 0


    # zeroing out the 1st row and col to 0
    if matrix[0][0] == 0:                 #check if origin of matrix is 0
        for r in range(rows):
             matrix[r][0] = 0                    #set the 1st col to 0

    if rowZeros:                         # check if  True
        for c in range(cols):
            matrix[0][c] = 0              #set the 1st row to 0

    return matrix


    
matrix = [[1,1,1], [1,0,1],[1,1,1] ]
print(setZeros(matrix))

    

