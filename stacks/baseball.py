def operations(ops):
    stack = []
    for op in ops:
        if op == "=":
            stack.append(stack[-1]+stack[-2])
        if op == "D":
            stack.append(2*stack[-1])
        if op == "C":
            stack.pop()
        if op.isdigit():
            stack.append(int(op))
    return sum(stack)
print(operations(["5","2","C","D","+"]))  # Output: 30 (stack after operations: [5, 10, 15])