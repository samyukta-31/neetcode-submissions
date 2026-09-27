class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token in ("+","-","/","*"):
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                if token == "+":
                    num = num1 + num2
                elif token == "-":
                    num = num1 - num2
                elif token == "/":
                    num = int(num1 / num2)
                elif token == "*":
                    num = num1 * num2
                num_stack.append(num)
            else:
                num_stack.append(int(token))
        return num_stack.pop()
                
            
        