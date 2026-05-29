class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        hash_table = {'}':'{', ')': "(", "]": '['}


        for i in s:
            if i not in hash_table:
                stack.append(i)
            else:
                check = hash_table[i]
                if stack and check == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False


        