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