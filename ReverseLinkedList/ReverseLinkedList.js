//! Optimized Approach:
//! Use Two Pointers
//! Instantiate two pointers one on the head and one pointing to null
//! while currPointer is pointing to a node
//! Store the original next connection
//! Overwrite the currNode's.next to be the prevNode
//! Set prevNode to currNode
//! Set currNode to original next connection
//! Return prevNode

//! Standard approach
//* Time O(n) | Space O(1)
const reverseList = head => {
	let currNode = head;
	let prevNode = null;
	while(currNode) {
	let ogNext = currNode.next;
	currNode.next = prevNode;
	prevNode = currNode;
	currNode = ogNext;
}
return prevNode;
}



//? Input: 0->1->2->3->null
//? NewList: 3->2->1->0->null

//! Recursive Approach
//* Time O(n) | Space O(n)
const reverseListRec = head => {
	if (!head) return null;
	let newHead = head; //0//1//2//3
	if (head.next) {
		newHead = reverseListRec(head.next);//0
		head.next.next = head;
}
head.next = null
return newHead
}
