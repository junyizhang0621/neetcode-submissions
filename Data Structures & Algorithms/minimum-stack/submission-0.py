class MinStack:

    def __init__(self):
        self.min_n = float('inf')
        self.min_stack = []
        self.elem = []
        

    def push(self, val: int) -> None:
        self.elem.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            cur_min = self.min_stack[-1]
            self.min_stack.append(min(cur_min, val))

    def pop(self) -> None:
        popped = self.elem.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.elem[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
