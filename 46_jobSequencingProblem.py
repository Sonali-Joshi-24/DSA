# Time Complexity: O(N log N) + O(N*M). and Space: O(M)

class job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

class Solution:
    def jobSchedulling(self, jobs):

        # sort the jobs in descending based on profit
        jobs.sort(key=lambda x: x.profit, reverse=True)
        # find the len of arr (maximum)
        maxi = jobs[0].deadline
        for i in range(1, len(jobs)):
            maxi = max(maxi, jobs[i].deadline)

        # initialize the maxi arr with -1
        slot = [-1] * (maxi + 1)
        countJobs = 0
        jobProfit = 0

        # fill the array
        for i in range(len(jobs)):
            for j in range(jobs[i].deadline , 0, -1):
                if slot[j] == -1:
                    slot[j] = i

                    countJobs += 1
                    jobProfit += jobs[i].profit
                    break
        return countJobs, jobProfit
    
if __name__ == "__main__":
    jobs = [job(1, 4, 20), job(2, 1, 10), job(3, 2, 40), job(4, 2, 30)]
    count, profit = Solution().jobSchedulling(jobs)
    print(count, profit)