class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        max_profit = 0

        for j in range(0, len(prices)):
            if prices[j] > prices[i]:
                window = prices[j] - prices[i]
                max_profit = max(window, max_profit)
            else:
                i = j
            j += 1

        return max_profit
        