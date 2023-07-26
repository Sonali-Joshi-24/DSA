# Time : O(NlogN) Space: O(1)
def minimumPlatform(arrival, depature, n):
    arrival.sort()
    depature.sort()
    count = 0
    ans = 0
    i , j = 0, 0
    while i < n:
        if arrival[i] <= depature[j]:
            count += 1
            ans = max(ans, count)
            i += 1
        elif arrival[i] > depature[j]:
            count -= 1
            j += 1
    return ans

arrival = [900, 940, 950, 1100, 1500, 1800]
# arrival = [900, 1100, 1235]
depature = [910, 1200, 1120, 1130, 1900, 2000]
# depature = [1000, 1200, 1240]
n = len(arrival)

print(minimumPlatform(arrival, depature, n))