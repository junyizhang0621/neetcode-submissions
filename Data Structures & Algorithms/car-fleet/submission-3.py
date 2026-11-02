class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time_arr = []

        for i in range(len(position)):
            time_arr.append((position[i], speed[i]))

        time_arr.sort()
        stack = []

        for p, s in time_arr:
            time = (target - p) / s

            while stack and stack[-1] <= time:
                stack.pop()

            stack.append(time)

        return len(stack)