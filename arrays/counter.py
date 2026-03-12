from collections import Counter

def count(arr):
    return dict(Counter(arr))
print(count([1, 2, 2, 3, 3, 3]))