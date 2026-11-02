class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0 

        stack = []

        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                stack.append(int(i))
            else:

                nums1 = stack.pop()
                nums2 = stack.pop()
                if i == "+":
                    stack.append(nums1 + nums2)
                elif i == "*":
                    stack.append(nums1 * nums2)
                elif i == "/":
                    stack.append(int(nums2 /nums1))
                elif i == "-":
                    stack.append(nums2 - nums1)
        
        return stack[-1]
                
        