class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0

        i, j = 0, 0

        hold = False

        while j < len(prices):
            if prices[j] == prices[i]:
                j += 1
            
            elif prices[i] < prices[j]:
                total += (prices[j] - prices[i])
                i = j
                j += 1
            else:
                i += 1
        
        return total
    