class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        # bruteforce
        # maxProfit = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i+1, len(prices)):
        #         sell = prices[j]
        #         maxProfit = max(maxProfit, sell-buy)

        # return maxProfit

        # Another way to start 2 pointers
        # maxProfit = 0
        # for l in range(len(prices)):
        #     buy = prices[l]
        #     for r in range(l+1, len(prices)):
        #         sell = prices[r]
        #         profit = sell - buy
        #         maxProfit = max(maxProfit, profit)
        # return maxProfit

        # 2 pointers
        maxProfit = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r+=1

        return maxProfit