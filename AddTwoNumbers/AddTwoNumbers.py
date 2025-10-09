class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy = ListNode()
    curr = dummy
    p, q = l1, l2

    while p or q or carry:
        x = p.val if p else 0
        y = q.val if q else 0
        s = x + y + carry
        carry = s // 10
        curr.next = ListNode(s % 10)
        curr = curr.next
        p = p.next if p else None
        q = q.next if q else None

    return dummy.next
