# Time: O(NlogN) + N and Space: O(1)

class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

class Solution:
    def fractionalKnapsack(self, W, arr, n):
        arr.sort(key=lambda x : x.value / x.weight, reverse = True)

        currWeight = 0
        finalValue = 0.0

        for i in range(n):
            if currWeight + arr[i].weight < W:
                currWeight += arr[i].weight
                finalValue += arr[i].value

            else:
                remain = W - currWeight
                finalValue += arr[i].value / arr[i].weight * remain
                break
        return finalValue
    

if __name__ == "__main__":
    n = 3
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
    ans = Solution().fractionalKnapsack(W, arr, n)
    print(ans)