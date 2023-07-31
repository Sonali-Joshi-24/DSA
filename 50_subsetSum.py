# Time Complexity: O(2^n)+O(2^n log(2^n)) and Space: O(2^n)
class Solution:
    def subsetSums(self, arr, n):
        ans = []
        
        def subsetSumHelper(ind, sum):
            # base case to return sum
            if ind == n:
                ans.append(sum)
                return
            
            # if element is picked
            subsetSumHelper(ind + 1, sum + arr[ind])
            # if not picked
            subsetSumHelper(ind + 1, sum)
        subsetSumHelper(0, 0)
        
        ans.sort()
        return ans
    
if __name__ == "__main__":
    arr = [3,1,2]
    n = len(arr)
    ans = Solution().subsetSums(arr, n)
    print(ans)


