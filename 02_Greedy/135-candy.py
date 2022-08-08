def candy(ratings):
    size = len(ratings)
    if size < 2:
        return size
    
    num = [1] * size

    for i in range(1, size):
        if ratings[i] > ratings[i-1]:
            num[i] = num[i-1] + 1

    for i in range(size - 1, 0, -1):
        if ratings[i-1] > ratings[i]:
            num[i-1] = max(num[i-1] + 1, num[i])

    return sum(num)


# Test
print(candy([1, 0, 2]))
# Output: 5
print(candy([1, 2, 2]))
# Output: 4
