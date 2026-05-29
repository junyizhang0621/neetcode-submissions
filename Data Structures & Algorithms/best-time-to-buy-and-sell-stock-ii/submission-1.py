class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        result = 0

        i, j = 0, 1

        while j < len(prices):
            buy = prices[i]
            sell = prices[j]

            if buy > sell:
                i+=1
                j+=1
            else:
                result += (sell - buy)
                j += 1
                i += 1
            
        return result
