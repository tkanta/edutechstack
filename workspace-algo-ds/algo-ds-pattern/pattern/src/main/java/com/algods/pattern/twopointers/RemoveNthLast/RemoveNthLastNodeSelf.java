package com.algods.pattern.twopointers.RemoveNthLast;

public class RemoveNthLastNodeSelf {

	/**
	 * Review Code: 
	 * 
	 * The removeNthLastNode function appears to be implemented
	 * correctly using the two pointers pattern. It correctly identifies the Nth
	 * last node by moving the right pointer N positions ahead of the left pointer.
	 * Then, it moves both pointers simultaneously until the right pointer reaches
	 * the end of the linked list. Finally, it removes the Nth last node by updating
	 * the next reference of the left pointer.
	 * 
	 * However, there are a few improvements that can be made to the code:
	 * 
	 * The function should handle the case where n is greater than the length of the
	 * linked list. Currently, it assumes that n is always a valid index. You can
	 * add a check at the beginning of the function to handle this case and return
	 * the original linked list unchanged.
	 * 
	 * The function could benefit from some additional comments to explain the logic
	 * and purpose of each step. This will make the code more readable and easier to
	 * understand for other developers.
	 * 
	 * The function could be made more generic by accepting a LinkedList object
	 * instead of a LinkedListNode object as the parameter. This would allow the
	 * function to work with any linked list, not just the one created using the
	 * LinkedList class provided.
	 * 
	 * Overall, the implementation is correct and follows the two pointers pattern
	 * effectively. With the suggested improvements, the code will be more robust
	 * and maintainable.
	 * 
	 * Time Complexity:
	 * -----------------
	 * The time complexity of the removeNthLastNode function is O(N), where N is the
	 * length of the linked list. This is because the function iterates through the
	 * linked list twice - once to find the nth node from the end, and once to
	 * remove it.
	 * 
	 * The time complexity of the built-in Java functions invoked by the code is as
	 * follows:
	 * 
	 * LinkedListNode.next: O(1) - accessing the next pointer of a linked list node
	 * is a constant time operation. LinkedListNode.data: O(1) - accessing the data
	 * field of a linked list node is a constant time operation. LinkedListNode.next
	 * = null: O(1) - assigning null to the next pointer of a linked list node is a
	 * constant time operation. LinkedListNode(int data): O(1) - creating a new
	 * linked list node with a given data value is a constant time operation.
	 * LinkedList.insertNodeAtHead: O(1) - inserting a node at the head of a linked
	 * list is a constant time operation. LinkedList. createLinkedList: O(N) -
	 * creating a linked list from an array of length N involves inserting N nodes
	 * at the head, which takes O(1) time per insertion. Therefore, the overall time
	 * complexity is O(N).
	 * 
	 * 
	 * Space Complexity: 
	 * -----------------
	 * The space complexity of the removeNthLastNode function is
	 * O(1) because it only uses a constant amount of additional space to store the
	 * left and right pointers.
	 * 
	 * The space complexity of the built-in Java functions invoked by the code is as
	 * follows:
	 * 
	 * The LinkedListNode class has a space complexity of O(1) because it only
	 * stores the data and next pointers. The LinkedList class has a space
	 * complexity of O(1) because it only stores the head pointer. The
	 * insertNodeAtHead method has a space complexity of O(1) because it only
	 * modifies the next pointer of the new node and the head pointer of the linked
	 * list. The createLinkedList method has a space complexity of O(1) because it
	 * only creates new nodes and inserts them at the head of the linked list.
	 * 
	 * @param head
	 * @param n
	 * @return
	 */
	
	// Code needs change
	// two different scenario needs to be handled for right == null and right=last element
	// In both of theses above scenario left == head
	public static LinkedListNode removeNthLastNode(LinkedListNode head, int n) {

		LinkedListNode left = head;
		LinkedListNode right = head;

		for (int i = 0; i < n; i++) {
			//if (right != null)
				right = right.next;
			//else
				//return head.next;
		}
		if(right == null)
			return head.next;	
		
		while (right != null && right.next != null) {
			left = left.next;
			right = right.next;
		}
		
		
//		if (left == head  && right.next != null) {
//			head = head.next;
//		} else {
			left.next = left.next.next;
		//}

		return head;
	}

//Driver Code
	public static void main(String[] args) {
		int[][] inputs = { { 23, 89, 10, 5, 67, 39, 70, 28 }, { 34, 53, 6, 95, 38, 28, 17, 63, 16, 76 },
				{ 288, 224, 275, 390, 4, 383, 330, 60, 193 }, { 1, 2, 3, 4, 5, 6, 7, 8, 9 },
				{ 69, 8, 49, 106, 116, 112, 104, 129, 39, 14, 27, 12 } };

		int[] n = { 4, 1, 6, 9, 11 };

		for (int i = 0; i < inputs.length; i++) {
			LinkedList<Integer> inputLinkedList = new LinkedList<Integer>();
			inputLinkedList.createLinkedList(inputs[i]);
			System.out.print((i + 1) + ".\tLinked List:\t\t");
			PrintList.printListWithForwardArrow(inputLinkedList.head);
			System.out.print("\n\tn = " + n[i]);
			System.out.print("\n\tUpdated Linked List:\t");
			PrintList.printListWithForwardArrow(removeNthLastNode(inputLinkedList.head, n[i]));
			System.out.println();
			System.out.println(new String(new char[100]).replace('\0', '-'));
		}
	}
}
