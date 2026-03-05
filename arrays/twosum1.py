## brute force for checking the sum of two numbers in an array is equal to the target or not
def sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in  range(i+1,n):
            if arr[i] + arr[j] == target:
                return True 
        return False
print(sum([1,2,3,4],5))

def sum2(arr,target):
    n = len(arr)
    for i in range(n):
        for j in  range(i+1,n):
            if arr[i] + arr[j] == target:
                return [i,j]
        return False
print(sum2([1,2,3,4],5))


## usinf hashing for checking the sum of two numbers in an array is equal to the target or not
def sum3(arr,target):
    hashset = set()
    n = len(arr)
    for i in range(n):
        if target - arr[i] in hashset:
            return True 
        hashset.add(arr[i])
    return False
print(sum3([1,2,3,4],5))

## usin the hashing to print the indices of the two numbers in an array whose sum is equal to the target
def sum4(arr,target):
    hashset = {}
    n = len(arr)
    for i in range(n):
        if target - arr[i] in hashset:
            return [hashset[target - arr[i]],i]
        hashset[arr[i]] = i
    return False
print(sum4([1,2,3,4],5))
