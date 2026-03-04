def count_freq(arr):
    freq = {}
    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]] = 1 
    return freq
print(count_freq([1,2,2,3,1,4]))


#### using counter 

