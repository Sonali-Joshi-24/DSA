'''
 The time complexity should indeed be O(NlogN) due to the usage of a hashmap. When inserting or searching for a key in the hashmap, it typically takes O(logN) time on average. Therefore, the overall time complexity becomes O(NlogN).

The space complexity remains the same at O(N) since we still need to store the frequencies of XOR values encountered in the hashmap.
'''

def subArrWithXOR(arr, b):
    freq = {}
    count = 0
    xorr = 0

    for i in arr:
        xorr ^= i

        # check if there is a subarray with xor equal to b
        if xorr == b:
            count += 1
            
        if xorr ^ b in freq:
            count += freq[xorr ^ b]

        # update the xor frequnecy dict
        if xorr in freq:
            freq[xorr] += 1
        else:
            freq[xorr] = 1

    return count



arr = [4,2,2,6,4]
b = 6
print(subArrWithXOR(arr,b))