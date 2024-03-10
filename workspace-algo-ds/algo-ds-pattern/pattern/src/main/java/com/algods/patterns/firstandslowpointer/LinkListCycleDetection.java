package com.algods.patterns.firstandslowpointer;


/**
 * Time complexity O(n), where n is the number of nodes in Linked List
 * Space complexity O(1)
 * @author tarin
 *
 */
public class LinkListCycleDetection {
	
	public static boolean isCyclePresent(LinkListNode<Integer> head) {
		
		if(head == null) {
			return false;
		}
		
		LinkListNode<Integer> slow = head;
		LinkListNode<Integer> fast = head;
		
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
			
			if(fast == slow) {
				return true;
			}
		}
		return false;
	}
	
	
	public static void main(String[] args) {
		LinkList<Integer> list = new LinkList<>();
		Integer[] intArr = {2,3,4,5,6};
		
		list.createLinkList(intArr);
		list.printList();
		
		System.out.println("\n------- Cycle present ? -----------------");
		System.out.println(isCyclePresent(list.head));
		
		System.out.println("\n------- Cycle present ? -----------------");
		list.createCycle(2);
		System.out.println(isCyclePresent(list.head));
	}
}
