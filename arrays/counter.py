from collections import Counter
def count_occurrences(arr):
    return dict(Counter(arr))
print(count_occurrences([1,2,2,3,3,3]))
## Output: Counter({3: 3, 2: 2, 1: 1})
