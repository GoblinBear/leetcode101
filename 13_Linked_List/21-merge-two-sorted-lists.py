class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_list(head):
    current = head
    while current:
        print(f'{current.val} ', end='')
        current = current.next
    
    print()


def merge_two_lists(list1, list2):
    dummy = ListNode(0, None)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next


# Test
print_list(merge_two_lists(ListNode(1, ListNode(2, ListNode(4, None))),
                           ListNode(1, ListNode(3, ListNode(4, None)))))
# Output: [1,1,2,3,4,4]
print_list(merge_two_lists(None, None))
# Output: []
print_list(merge_two_lists(None, ListNode(0, None)))
# Output: [0]
