class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if len(temperatures) <= 1:
            return [0]

        stack = []
        result = [0] * len(temperatures)


        for i in range(len(temperatures)):
            if not stack:
                stack.append((temperatures[i], i))
                continue

            
            while stack and stack[-1][0] < temperatures[i]:
                curT, index = stack[-1]
                result[index] = i - index
                stack.pop()
            
            stack.append((temperatures[i], i))
            
        return result




        