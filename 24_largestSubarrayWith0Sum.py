'''
input : n = 8
        array = {15,-2,2,-8,1,7,10,23}
output : 5
Explanation : The largest subarray with sum 0 will be -2,2,-8,1,7


naive solution: generate all the sub-arrays and compare which sub-arr gives us solution 0 
note: to generate sub-arrays use kadane's algorithm

'''

# naive approach
# using kadane's algorithm : O(n^3) and space: O(n) || but thsi code won't work for all output 


# Time : O(nlogn) Space: O(n) || hash-mqp 

def max_len(arr):
    prefix_sum = {}
    max_length = 0

    current_sum = 0

    for i , num in enumerate(arr):
        current_sum += num

        if current_sum == 0:
            max_length = i + 1  #from the 1st element to current index it is giving sum as 0 
        
        if current_sum in prefix_sum:
            length = i - prefix_sum[current_sum]
            max_length = max(length, max_length)
        
        else:
            prefix_sum[current_sum] = i
    return max_length


# efficient approach 
arr = [15,-2,2,-8,1,7,10,23]
print(max_len(arr))






