def generate(n,curr,result):
    if len(curr) == n:
        result.append(curr)
        return 

    generate(n,curr + "0", result)
    if not curr or curr[-1] != "1":
        generate(n,curr + "1", result)
def main():
    n = 4
    result = []
    generate(n," ", result)
    print(result)
if __name__ == "__main__":
    main()
        