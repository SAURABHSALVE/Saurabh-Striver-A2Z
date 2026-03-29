""""problem statement: Given an array of integers, 
return an array where each element at index i is the product of all the 
elements in the original array except the one at index i."""

""""solution: We can solve this problem by using two passes through the array.
In the first pass, we can calculate the prefix product for each element,
which is the product of all the elements to the left of the current element.
In the second pass, we can calculate the suffix product for each element, 
which is the product of all the elements to the right of the current element.
Finally, we can multiply the prefix and suffix products to get the desired result."""

def product(arr):
    n = len(arr)
    res = [1]*n 
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(n-1,-1,-1):
        res[i] *= suffix 
        suffix *=arr[i]
    return res 
print(product([1,2,3,4]))
       
       
## command to run this file 
# python product_of_array.py


"""explanation:
The function `product` takes an array `arr` as input and returns a 
new array where each element at index `i` is the product of all the
elements in the original array except the one at index `i`."""