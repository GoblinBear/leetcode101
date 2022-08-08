def lower_bound(nums, target):
    left = 0
    right = len(nums)
    mid = 0

    while left < right:
        mid = left + int((right - left) / 2)
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    
    return left


def upper_bound(nums, target):
    left = 0
    right = len(nums)
    mid = 0

    while left < right:
        mid = left + int((right - left) / 2)
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    
    return left


def search_range(nums, target):
    size = len(nums)
    if size == 0:
        return [-1, -1]

    lower = lower_bound(nums, target)
    upper = upper_bound(nums, target) - 1
    if lower == size or nums[lower] != target:
        return [-1, -1]

    return [lower, upper]


# Test
print(search_range([5, 7, 7, 8, 8, 10], 8))
# Output: [3, 4]
print(search_range([5, 7, 7, 8, 8, 10], 6))
# Output: [-1, -1]
print(search_range([], 0))
# Output: [-1, -1]
