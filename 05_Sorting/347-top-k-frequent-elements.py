def top_k_frequent(nums, k):
    counts = {}
    max_count = 0

    for num in nums:
        if num in counts:
            counts[num] = counts[num] + 1
        else:
            counts[num] = 1

        max_count = max(max_count, counts[num])

    buckets = [[]] * (max_count + 1)
    for num, count in counts.items():
        buckets[count].append(num)
    
    ans = []
    i = max_count
    while i >= 0 and len(ans) < k:
        for num in buckets[i]:
            ans.append(num)
            if len(ans) == k:
                break

        i = i - 1

    return ans


# Test
print(top_k_frequent([1,1,1,2,2,3], 2))
# Output: [1,2]
print(top_k_frequent([1], 1))
# Output: [1]
