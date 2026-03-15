# def rotate(nums,k):
#     n = len(nums)
#     k = k % n
#     l = 0
#     r = n-1
#     while l < r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l+=1
#         r-=1
#     l = 0
#     r = k-1
#     while l < r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l+=1
#         r-=1
#     l = k
#     r = n-1
#     while l < r:
#         nums[l],nums[r] = nums[r],nums[l]
#         l+=1
#         r-=1
#     return nums
# print(rotate([1,2,3,4,5,6,7],3))


## solution using helper function
def reverse(nums,l,r):
    while l<r:
        nums[l],nums[r] = nums[r],nums[l]
        l+=1
        r-=1 
def rotate(nums,k):
    n = len(nums)
    k = k % n
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums
print(rotate([1,2,3,4,5,6,7],3))