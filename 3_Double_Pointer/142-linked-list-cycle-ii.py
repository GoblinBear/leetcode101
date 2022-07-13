class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head
    
    def append(self, value):
        new_node = ListNode(value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        
        return new_node


def detect_cycle(head):
    slow = head
    fast = head
    
    while True:
        if (not fast) or (not fast.next) or (not fast.next.next):
            return None
        
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            break

    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next

    return fast

        
# Test
linked_list1 = LinkedList()
linked_list1.append(3)
cycle_node1 = linked_list1.append(2)
linked_list1.append(0)
cycle_node2 = linked_list1.append(-4)
cycle_node2.next = cycle_node1
node = detect_cycle(linked_list1.get_head())
if node:
    print(node.value)
else:
    print(None)
# Output: index = 1, value = 2

linked_list2 = LinkedList()
cycle_node1 = linked_list2.append(1)
cycle_node2 = linked_list2.append(2)
cycle_node2.next = cycle_node1
node = detect_cycle(linked_list2.get_head())
if node:
    print(node.value)
else:
    print(None)
# Output: index = 0, value = 1

linked_list3 = LinkedList()
linked_list3.append(1)
node = detect_cycle(linked_list3.get_head())
if node:
    print(node.value)
else:
    print(None)
# Output: index = -1, value = None
