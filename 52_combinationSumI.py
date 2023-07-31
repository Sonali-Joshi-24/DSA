class Solution:
    def combinationSum(self, candidate, target):
        res = []

        def dfs(i, cur, total):
            # base case
            if total == target:
                res.append(cur[::])
                return
            
            if i >= len(candidate) or total > target:
                return
            
            # include val at candidate
            cur.append(candidate[i])
            dfs(i, cur, total + candidate[i])
            cur.pop()

            # can't include the candidate
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
    
ans = Solution()
candidate = [2, 3, 6, 7]
target = 7
print(ans.combinationSum(candidate, target))
