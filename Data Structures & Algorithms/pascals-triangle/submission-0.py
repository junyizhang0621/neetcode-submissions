class Solution:
    def generate(self, numRows: int) -> List[List[int]]:


        dp = [[1]]

        for i in range(numRows-1):
            temp =[0] + dp[-1] + [0]
            row = []
            for j in range(len(dp[-1]) + 1):
                row.append(temp[j] + temp[j+1]) 
            dp.append(row)
        
        return dp

        # def dfs(i):
        #     if i == 1:
        #         dp[[i]] = [1]
        #         return [1]
            
        #     if i in dp[i]:
        #         return dp[i]

        #     result = dfs(i-1)
        #     cur = []
