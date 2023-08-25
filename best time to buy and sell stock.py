class Solution:
    def maxProfit(self, prices) -> int:
        t = sorted(prices, reverse=True)
        print(t, prices)
a = Solution()
a.maxProfit([1, 5, 7, 9, 2, 35, 6])
