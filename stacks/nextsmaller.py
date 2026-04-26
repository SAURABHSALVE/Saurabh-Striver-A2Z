def smaller(arr):
    sme = [-1]*len(arr)
    stack = []
    for i in range(len(arr)-1,-1,-1):
        while stack and stack[-1]>=arr[i]:
            stack.pop()
        if stack:
            sme[i] = stack[-1]
        stack.append(arr[i])
    return sme
print(smaller([4,5,2,10,8]))


## python implementation of next smaller element to the right
### command to run: python nextsmaller.py