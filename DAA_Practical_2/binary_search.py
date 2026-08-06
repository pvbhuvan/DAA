def bsearch(nums,target):
    left=0
    right = len(nums)-1
    while left<=right:
        mid = (left+ right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
    return -1
nums = eval(input())
target = int(input())
result = bsearch(nums,target)
if result != -1:
    print("found at : ",result)
else:
    print("not found")
