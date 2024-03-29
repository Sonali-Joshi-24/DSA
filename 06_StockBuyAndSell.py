'''
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Time Complexity: O(N) and Space Complexity : O(1)
'''


def maxProfit(prices):
    max_profit = 0
    min_price = float('inf')

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price-min_price)
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))



# print(min(float("inf"), 7))
# profit = price - min_price       #price on which I am currently on - min_price
