# def count_freq(arr):
#     freq = {}
#     n = len(arr)
#     for i in range(n):
#         if arr[i] in freq:
#             freq[arr[i]]+=1
#         else:
#             freq[arr[i]] = 1 
#     return freq
# print(count_freq([1,2,2,3,1,4]))

from collections import Counter 

def count(arr):
    freq =dict(Counter(arr))  ## useed type casting to convert the counter object to a dictionary
    return freq    ## the counter object is a subclass of dictionary that provides a convenient way to count the occurrences of elements in a collection. By converting it to a regular dictionary, we can easily access the frequency of each element.
print(count([1,2,2,3,1,4])) ## Output: {1: 2, 2: 2, 3: 1, 4: 1}
