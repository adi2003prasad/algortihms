class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxPr = 0
        dup = prices
        if(dup.sort(reverse=True)==prices):return 0
        while(len(prices)>1):
            buy = min(prices)
            # print("buy", buy)
            if(prices[-1]==buy):
                prices.pop()
                continue
            
            buyIndex = prices.index(buy)
            sell = max(prices[buyIndex:]) # finding the loacal maxima in current available future
            # print("wtf", sell, max(prices))
            if(buy==sell):
                prices = prices[:buyIndex-1]
                continue
            if(sell==max(prices)):
                if(prices[0]==sell):prices.pop(0)
                if(maxPr>sell-buy):pass
                else:return sell-buy
            curDraw = sell-buy
            # print(buy, sell)
            if(curDraw>maxPr):maxPr = curDraw
            prices.pop(buyIndex)
            # print(prices)
        # print(prices)
        return maxPr
    def maxprofit(self, prices):
        leftPointer = 0
        rightPointer = 1
        maxpr = 0
        while(rightPointer<len(prices)):
            buy = prices[leftPointer]
            sell = prices[rightPointer]
            if(sell<buy):
                leftPointer +=1
                ri
            
            
            
a = Solution()
print(a.maxProfit([9, 7, 5, 3, 1, 4]))