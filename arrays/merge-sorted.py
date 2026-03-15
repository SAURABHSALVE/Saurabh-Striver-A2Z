def merge(arr1,arr2,m,n):
    i = m-1
    j = n-1
    insert = len(arr1)-1
    while i >= 0 and j >=0:
        if arr1[i] > arr2[j]:
            arr1[insert] = arr1[i]
            i-=1
        else:
            arr1[insert] = arr2[j]
            j-=1
        insert-=1
    while j >=0:
        arr1[insert] = arr2[j]
        j-=1
        insert-=1
arr1 = [1,2,3,0,0,0]
arr2 = [2,5,6]
merge(arr1,arr2,3,3)
print(arr1)
