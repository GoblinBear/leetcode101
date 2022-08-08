def two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            break
        if sum < target:
            left = left + 1
        else:
            right = right - 1

    return [left + 1, right + 1]


# Test
print(two_sum([2,7,11,15], 9))
# Output: [1, 2]
print(two_sum([2,3,4], 6))
# Output: [1,3]
print(two_sum([-1,0], -1))
# Output: [1, 2]
