def two_sum(nums, target):
    hash = {}
    ans = []

    for i, num in enumerate(nums):
        if target - num in hash:
            ans.append(hash[target - num])
            ans.append(i)
            break
        else:
            hash[num] = i

    return ans


# Test
print(two_sum([2,7,11,15], 9))
# Output: [0,1]
print(two_sum([3,2,4], 6))
# Output: [1,2]
print(two_sum([3,3], 6))
# Output: [0,1]
