class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            add = True
            # a is moving left and top of stack is moving right -> collision
            while stack and a < 0 and stack[-1] > 0:
                top = stack[-1]
                if top < -a:          # incoming wins, top explodes
                    stack.pop()
                    # keep looping: a may collide with the new top
                elif top == -a:       # both explode
                    stack.pop()
                    add = False
                    break
                else:                  # top wins, a explodes
                    add = False
                    break
            if add:
                stack.append(a)

        return stack


        