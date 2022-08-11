import itertools

class NumArray:
    def __init__(self, nums):
        self.sum = list(itertools.accumulate(nums))

    def sum_range(self, left, right):
        if left == 0:
            return self.sum[right]

        return self.sum[right] - self.sum[left - 1]


# Test
num_array = NumArray([1, 2, 3, 4, 5])
print(num_array.sum_range(0, 3))
# Output: 10
print(num_array.sum_range(1, 3))
# Output: 9
print(num_array.sum_range(2, 4))
# Output: 12
