class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        # Use a set for O(1) operator lookups
        operators = {"+", "-", "*", "/"}
        
        for token in tokens:
            if token not in operators:
                # If it's a number, push it onto the stack
                stack.append(int(token))
            else:
                # If it's an operator, pop the two most recent operands
                right = stack.pop()
                left = stack.pop()
                
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    # Division must truncate toward zero per RPN rules
                    # In Python, int(left / right) handles this correctly
                    stack.append(int(float(left) / right))
        
        # The last remaining element is the result
        return stack.pop()