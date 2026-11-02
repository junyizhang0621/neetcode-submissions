class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        check_dict = {'(': ")", "[":"]", "{": "}"}


        for i in s:
            if i in check_dict.keys():
                stack.append(i)
            else:
                if stack and check_dict[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False
                


