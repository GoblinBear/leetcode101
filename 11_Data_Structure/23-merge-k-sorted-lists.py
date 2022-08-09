import heapq


def merge_k_lists(lists):
    if not lists:
        return []

    ans = []
    heapq.heapify(lists)
    priority_queue = lists

    while priority_queue:
        min_list = heapq.heappop(priority_queue)
        
        if min_list:
            min_value = min_list.pop(0)
            ans.append(min_value)
            heapq.heappush(priority_queue, min_list)

    return ans


# Test
print(merge_k_lists([[1,4,5],[1,3,4],[2,6]]))
# Output: [1,1,2,3,4,4,5,6]
print(merge_k_lists([]))
# Output: []
print(merge_k_lists([[]]))
# Output: []
