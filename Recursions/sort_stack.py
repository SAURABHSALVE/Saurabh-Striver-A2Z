def insert(stack, temp):
    # Base case: if the stack is empty or temp is larger than the top element
    if not stack or stack[-1] <= temp:
        stack.append(temp)
        return
    
    # Pop the top element and recursively insert
    val = stack.pop()
    insert(stack, temp)
    
    # Push the popped element back
    stack.append(val)

def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insert(stack, temp)

# Main function
if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    sortStack(stack)

    # Print the sorted stack
    print("Sorted stack (descending order):", stack)
