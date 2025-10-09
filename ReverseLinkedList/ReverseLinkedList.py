

#! Problem: Reverse a singly linked list
#? API for NODE: 
#? .val
#? .next

#!Example 3: 

#* input: 0-> 1 -> 2 ->3 -> null
#! output: 3 -> 2 -> 1 -> 0 -> null

#! 1. Set up two pointers one on the head and one pointing to null
#! 2. while the current pointer exists or pointing to a node
#!     a. we want to store the the orignal next connection
#!     b. we want to overwrite the currNode's.next to be the prevNode
#!     c. Set prevNode to currNode
#!     d. set currNode to original next connection

def reverseList(head)
    prev, curr = None, head
    while curr:
        nxt - curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def reverseListRecursive(head):
    if not head or not head.next:
        return head
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
