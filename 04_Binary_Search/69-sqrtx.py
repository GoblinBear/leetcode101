def my_sqrt1(x):
    if x == 0:
        return x
    left = 1
    right = x
    mid = 0
    sqrt = 0

    while left <= right:
        mid = left + int((right - left) / 2)
        sqrt = int(x / mid)
        if sqrt == mid:
            return mid
        elif mid > sqrt:
            right = mid - 1
        else:
            left = mid + 1

    return right


def my_sqrt2(a):
    x = a
    while x * x > a:
        x = int(int(x + a / x) / 2)
    
    return x


# Test
print(my_sqrt1(4))
# Output: 2
print(my_sqrt1(8))
# Output: 2
print(my_sqrt2(4))
# Output: 2
print(my_sqrt2(8))
# Output: 2
