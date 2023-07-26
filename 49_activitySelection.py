from typing import List

class meeting:
    def __init__(self, start, end, pos):
        self.start = start
        self.end = end
        self.pos = pos

class Solution:
    def findMaxMeetings(self, s:List[int], e: List[int], n: int):
        meet = [meeting(s[i], e[i], i + 1) for i in range(n)]
        sorted(meet, key=lambda x : (x.end, x.pos))
        ans = []

        meetLimit = meet[0].end
        ans.append(meet[0].pos)

        for i in range(1, n):
            if meet[i].start > meetLimit:
                meetLimit = meet[i].end
                ans.append(meet[i].pos)
        print("The order in which the meetings will be peformed is : ")
        return ans

if __name__ == "__main__":
    obj = Solution()
    n = 6
    start = [1, 3, 0, 5, 8, 5]
    end = [2, 4, 5, 7, 9, 9]
    print(obj.findMaxMeetings(start, end, n))
    

