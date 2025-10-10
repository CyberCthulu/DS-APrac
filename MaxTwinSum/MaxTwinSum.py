# 🧩 Pseudocode — Max Twin Sum of a Linked List

# Goal:
# Find the maximum sum of “twin nodes,” where the first half of the list is paired with the reversed second half.

# Step-by-step plan

# Find the midpoint of the list

# Use the “slow & fast pointer” technique.

# Move slow by 1 step, fast by 2 steps each iteration.

# When fast reaches the end, slow is at the start of the second half (since n is even).

# Reverse the second half of the list

# Use three pointers (prev, curr, next) to reverse links in place.

# After this step, you’ll have:

# First half: original order.

# Second half: reversed order (starting at prev).

# Use two pointers (left and right)

# left starts at head of first half.

# right starts at head of reversed second half.

# At each step:

# Compute left.val + right.val

# Track the maximum sum.

# Move both pointers forward until right ends (n/2 steps).

# Return the maximum twin sum.

c# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: ListNode) -> int:
    """
    Given the head of an even-length linked list, 
    return the maximum twin sum.
    """

    # Step 1️⃣: Find the midpoint using slow and fast pointers
    slow = fast = head
    # fast moves twice as fast; when fast hits end, slow is at mid
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # At this point, `slow` is the head of the second half of the list

    # Step 2️⃣: Reverse the second half of the list starting from `slow`
    prev = None
    curr = slow
    while curr:
        nxt = curr.next      # store the next node before we break the link
        curr.next = prev     # reverse pointer (make current point to previous)
        prev = curr          # move prev one step forward (prev = curr)
        curr = nxt           # move curr one step forward (curr = next)
    # After loop: `prev` now points to the head of the reversed half

    # Step 3️⃣: Initialize pointers for both halves
    left = head     # pointer at beginning of first half
    right = prev    # pointer at beginning of reversed second half
    max_sum = 0     # variable to track the maximum twin sum found

    # Step 4️⃣: Traverse both halves simultaneously
    while right:  # only need to traverse n/2 times
        twin_sum = left.val + right.val  # compute twin sum for the pair
        max_sum = max(max_sum, twin_sum) # update maximum if needed
        left = left.next                 # move to next node in first half
        right = right.next               # move to next node in reversed half

    # Step 5️⃣: Return the maximum twin sum after traversal
    return max_sum
