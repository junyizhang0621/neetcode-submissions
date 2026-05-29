class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            if not stack:
                stack.append(i)
            else:
                if stack[-1] * i > 0:
                    stack.append(i)
                else:
                    while stack and stack[-1] > 0 and i < 0:
                        if stack[-1] == abs(i):
                            stack.pop()
                            i = 0
                        elif abs(i) > stack[-1]:
                            stack.pop()
                        else:
                            i = 0
                    if i:
                        stack.append(i)    
        return stack
        