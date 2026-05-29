class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = set(['+', '-', '*', '/'])

        stacks = []

        for i in tokens:
            if i not in operation:
                stacks.append(i)
            else:
                first = int(stacks.pop())
                second = int(stacks.pop())
                print(i)
                print(second, first)
                if i == "+":
                    result = first + second
                    stacks.append(str(result))
                
                elif i == "-":
                    result = second - first
                    stacks.append(str(result))
                
                elif i == "*":
                    result = first * second
                    stacks.append(str(result))
                elif i == "/":
                    result = int(second / first)
                    stacks.append(str(result))
        return int(stacks[-1])
                
