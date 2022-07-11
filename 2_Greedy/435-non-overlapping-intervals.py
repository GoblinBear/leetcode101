def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    size = len(intervals)
    intervals.sort(key=lambda x: x[1])

    removed = 0
    prev = intervals[0][1]

    for i in range(1, size):
        if intervals[i][0] < prev:
            removed = removed + 1
        else:
            prev = intervals[i][1]

    return removed


# Test
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
# Output: 1
print(eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
# Output: 2
print(eraseOverlapIntervals([[1,2],[2,3]]))
# Output: 0
