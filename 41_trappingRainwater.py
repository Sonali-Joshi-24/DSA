'''
Time : O(N) and Space : O(N)

formula = min(l,r) - input
(note for negative res assume 0)

ans       0  0  1  0  1  2  1  0  0  1  0  0      = 1 + 1 + 2+ 1 + 1= 6
input    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
maxLeft   0  0  1  1  2  2  2  2  3  3  3  3
maxRight  3  3  3  3  3  3  3  2  2  2  1  0      start from end and compare maxright
min(l,r)  0  0  1  1  2  2  2  2  2  2  1  0

'''

'''
# Time : O(N) and space: O(1)
Two pointer approach

maxL = 0
maxR = 1
shift the pointer with smaller max val  
          

          L  L                             R
input    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
'''

def trappingWater(height):
    if not height: return 0

    l, r = 0, len(height) - 1
    leftMax, rightMax = height[l] , height[r]
    res = 0

    while l < r:
        if leftMax < rightMax:
            l += 1
            leftMax = max(leftMax, height[l])
            res += leftMax - height[l]
        else:
            r -= 1
            rightMax = max(rightMax, height[r])
            res += rightMax - height[r]

    return res
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trappingWater(height))


