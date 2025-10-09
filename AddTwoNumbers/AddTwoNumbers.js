// https://leetcode.com/problems/add-two-numbers/description/
// Add Two Numbers

// You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

// The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

// Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Return the sum of the two numbers as a linked list.

// Example 1:
// Input: l1 = [1,2,3], l2 = [4,5,6]

// Output: [5,7,9]

// Explanation: 321 + 654 = 975.

// Example 2:
// Input: l1 = [9], l2 = [9]

// Output: [8,1]

// Constraints:
// 1 <= l1.length, l2.length <= 100.
// 0 <= Node.val <= 9

// Example 3:
// Input: l1 = [1,2,4], l2 = [4,5,6]
// Output: [5,7,0,1]


// Naive Approach:
// Put numbers into an array in order
// Combine into a string and convert to integer
// Add integers
// Convert back to LL





// Optimized Approach:
// Add the digits of the two lists like we would in a math problem. Since we're planning to add starting from the 10s place the LLs being in reverse is to our advantage. Tricky part is handling the carry when our digits add to something greater than 10.

// Pseudocode:
// Create a dummy node for our output list
// Initialize the carry as zero
// while(list1 or list2 or carry exists):
// Add the values from L1 + L2 + carry
// Update the carry to be the first digit of sum by taking Math.floor(sum/10)
// Set sum to the remaining digit by taking sum%10
// Turn sum into a list node and set it as currResultNodes.next
// Iterate our pointers to the next node in each list
// Return dummy.next

// Input: l1 = [1,2,4], l2 = [4,5,6]
// 		        |             |

// Output: [5,7,0,1]

// Time O(max(l1,l2))
// Space O(max(l1,l2))

const addTwoNums = (l1, l2) => {
	const dummy = new ListNode();
	let curr = dummy;
	let carry = 0;
	
	while(l1 || l2 || carry) {
	const v1 = l1 ? l1.val : 0;
	const v2 = l2 ? l2.val : 0;
	
	let sum = v1 + v2 + carry;
	carry = Math.floor(sum/10);
	sum = sum % 10;
	
	curr.next = new ListNode(sum);
	curr = curr.next;
	l1 = l1 ? l1.next : null;
	l2 = l2 ? l2.next : null;
}
return dummy.next;
}
