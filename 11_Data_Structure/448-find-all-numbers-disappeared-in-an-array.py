def find_disappeared_numbers(nums):
    ans = []
    for num in nums:
        pos = abs(num) - 1
        if nums[pos] > 0:
            nums[pos] = -nums[pos]

    for i, num in enumerate(nums):
        if nums[i] > 0:
            ans.append(i + 1)

    return ans


# Test
print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
# Output: [5, 6]
print(find_disappeared_numbers([1, 1]))
# Output: [2]
