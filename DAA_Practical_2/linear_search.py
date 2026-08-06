def lsearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

nums = eval(input("Enter the list of numbers: "))
target = int(input("Enter the target element: "))

result = lsearch(nums, target)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")