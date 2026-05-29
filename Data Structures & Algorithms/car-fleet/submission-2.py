class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        dist = [(p, s) for p, s in zip(position, speed)]        
        dist.sort()
        dist = dist[::-1]

        stack = []

        for p, s in dist:
            stack.append((target - p)/s)
            if len(stack) >= 2:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)
         