def find_kth_largest(nums, k):
    n = len(nums)
    left = 0
    right = n - 1
    target = n - k

    while left < right:
        mid = quick_selection(nums, left, right)
        if mid == target:
            return nums[mid]
        
        if mid < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return nums[left]


def quick_selection(nums, left, right):
    i = left + 1
    j = right

    while True:
        while i < right and nums[i] <= nums[left]:
            i = i + 1

        while left < j and nums[j] >= nums[left]:
            j = j - 1

        if i >= j:
            break
        
        nums[i], nums[j] = nums[j], nums[i]
    
    nums[left], nums[j] = nums[j], nums[left]
    nums[:] = nums
    return j


# Test
print(find_kth_largest([3,2,1,5,6,4], 2))
# Output: 5
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))
# Output: 4
