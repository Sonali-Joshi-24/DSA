'''
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Solution:
1. take this intervals and sort them based on the start value   of each interval
2. iterate through each start value
3. keep checking does curr_intervals overlapps previous interval
4. if it does we can merge them into large interval
'''

def mergeIntervals(array):
    # Time : O(nlogn)
    array.sort(key = lambda i : i[0]) #sort by start value
    output = [array[0]]   #store the 1st sub-arry in output to avoid edge case

    for start, end  in array[1:]:      # start iterating from 1st index since oth index is alreday in output
        lastEnd = output[-1][1]        # the lastEle of the latest sub-arr

        if start <= lastEnd:               # check start <= last 
            output[-1][1] = max(lastEnd, end)   # update output lastEle of output to be max(of last ele of 2 sub arr)
        else:
            output.append([start, end])
    return output





# arr = [[1,2], [3,4], [5,6]]
# for start, end in arr[1 :]:
#     print(start, end)
    

# arr = [[1,3], [2,6], [11,15], [9,10]]
# arr.sort(key = lambda i : i[0])
# print(arr)


# item = [(3, "Apple"), (2, "mango"), (1, "banana")]
# sorted_items = sorted(item, key=lambda i: i[0])
# print(sorted_items)

# items = [[3, "B"], [2, "C"], [1, "A"]]
# items.sort(key=lambda i : i[1])
# print(items)