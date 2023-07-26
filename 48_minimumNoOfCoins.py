# Time Complexity : O(V) very less and Space: O(1)


def findMinimumCoins(V):
    ans = []
    coins = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(coins)

    for i in range(n - 1, 0, -1):
        while V >= coins[i]:
            V -= coins[i]
            ans.append(coins[i])
    return len(ans)

V = 70
print(findMinimumCoins(V))





