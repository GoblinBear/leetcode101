def merge(nums1, m, nums2, n):
    position = m + n - 1
    m = m - 1
    n = n - 1

    while m >= 0 and n >= 0:
        if nums1[m] > nums2[n]:
            nums1[position] = nums1[m]
            m = m - 1
        else:
            nums1[position] = nums2[n]
            n = n - 1

        position = position - 1

    while n >= 0:
        nums1[position] = nums2[n]
        position = position - 1
        n = n - 1

    return nums1


# Test
print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))
# Output: [1,2,2,3,5,6]
print(merge([1], 1, [], 0))
# Output: [1]
print(merge([0], 0, [1], 1))
# Output: [1]
