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


def reverse_list(head):
    previos = None
    next = None

    while head:
        next = head.next
        head.next = previos
        previos = head
        head = next

    return previos


# Test
print_list(reverse_list(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))))
# Output: [5,4,3,2,1]
print_list(reverse_list(ListNode(1, ListNode(2, None))))
# Output: [2,1]
print_list(reverse_list(None))
# Output: None
