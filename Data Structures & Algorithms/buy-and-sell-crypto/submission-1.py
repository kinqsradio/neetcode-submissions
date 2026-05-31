class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 2 pointers
        # l, r = 0, 1
        # maxProfit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         l=r

        #     r+=1

        # return maxProfit
        
        # bruteforce
        maxProfit = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1, len(prices)):
                sell = prices[j]
                maxProfit = max(maxProfit, sell-buy)

        return maxProfit