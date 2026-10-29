class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index = 0
        max = 0

        while index < len(prices):
            for price in prices[index + 1:]:
                if price > prices[index] and price - prices[index] > max:
                    max = price - prices[index]

            index += 1

        return max