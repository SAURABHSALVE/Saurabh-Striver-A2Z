def twosum(arr,target):
    n = len(arr)
    hashset = {}
    for i in range(n):
        curr = arr[i]
        need = target - arr[i]
        if need in hashset:
            return [hashset[need],i]
        hashset[curr] = i
    return []

print(twosum([1,2,3,4,5],4))