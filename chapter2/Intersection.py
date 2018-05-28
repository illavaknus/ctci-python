from LinkedList import LinkedList

def intersection(ll):
    if ll.head is None or ll.head.next is None:
        return None
    slow = ll.head
    fast = ll.head.next
    while slow and fast and fast.next:
        if slow == fast:
            break
        fast = fast.next.next
        slow = slow.next
    
    slow = ll.head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
        
