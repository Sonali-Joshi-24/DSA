# Time Complexity and Space Complexity : O(N^2)


def generate(numRows):
    # create the 1st row
    res = [[1]]

    for i in range(numRows - 1): #since we have already created the 1st row
        # add 0's to start and end of above row
        temp = [0] + res[-1] + [0]
        row = []  #next row

        for j in range(len(res[-1]) + 1):
            row.append(temp[j] + temp[j+1])
        res.append(row)
    return res

print(generate(5))







# explanation
# res = [[0],[0,1,0,1]]
# print(len(res[-1]) + 1)


 