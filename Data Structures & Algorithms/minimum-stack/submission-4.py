class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack = self.stack + [val]
        if not self.min_stack:
            self.min_stack = [val]
        else:
            if val <= self.min_stack[0]:
                self.min_stack = [val] + self.min_stack
            else:
                self.min_stack.append(val)

    def pop(self) -> None:
        popped = self.stack[-1]
        self.stack = self.stack[0:len(self.stack)-1]

        if popped == self.min_stack[0]:
            self.min_stack = self.min_stack[1:]
        elif popped == self.min_stack[-1]:
            self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(self.min_stack)
        return self.min_stack[0]
        
        
