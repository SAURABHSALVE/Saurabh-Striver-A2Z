def generate(n,curr,result):
    if len(curr) == n:
        result.append(curr)
        return 
    generate(n,curr + '0',result)
    
    if len(curr) == 0 or curr[-1] != '1':
        generate(n,curr + '1',result)

def main():
    n = 3
    result = []
    generate(n,'',result)
    print(result)
main()