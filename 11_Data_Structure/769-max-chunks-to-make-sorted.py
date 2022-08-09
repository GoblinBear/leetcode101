def max_chunks_to_sorted(arr):
    chunks = 0
    current_max = 0
    for i, element in enumerate(arr):
        current_max = max(current_max, arr[i])
        if current_max == i:
            chunks = chunks + 1

    return chunks


# Test
print(max_chunks_to_sorted([4,3,2,1,0]))
# Output: 1
print(max_chunks_to_sorted([1,0,2,3,4]))
# Output: 4
