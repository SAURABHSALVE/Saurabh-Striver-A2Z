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
def freq(arr):
    return dict(Counter(arr)) ## Counter returns a dictionary with the frequency of each element in the array. We convert it to a regular dictionary using dict().
print(freq([1,2,2,3,1,4]))

