# def backtrack(curr, open, close, n, res):
#     if len(curr) == 2 * n:
#         res.append(curr)
#         return
#     if open < n:
#         backtrack(curr + '(', open + 1, close, n, res)
#     if close < open:
#         backtrack(curr + ')', open, close + 1, n, res)

# def generate_parenthesis(n):
#     res = []
#     backtrack("", 0, 0, n, res)
#     return res

# def main():
#     result = generate_parenthesis(3)
#     for s in result:
#         print(s)

# if __name__ == "__main__":
#     main()

def is_valid(curr):
    balance = 0
    for char in curr:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0

def generate(n,curr,res):
    if len(curr) == 2 * n:
        if is_valid(curr):
            res.append(curr)
        return
    generate(n,curr + '(',res)
    generate(n,curr + ')',res)

def main():
    n = 3
    res = []
    generate(n,'',res)
    print(res)
    
    