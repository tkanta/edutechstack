package com.algods.patterns.firstandslowpointer;

/**
 * Time complexity O(n)
 * space complexity O(1)
 * @author tarin
 *
 */
public class LinkedListMiddleNode {

	public static LinkListNode<Integer> getMiddleNode(LinkListNode<Integer> head) {
		
		LinkListNode<Integer> slow = head;
		LinkListNode<Integer> fast = head;
		
		while(fast != null && fast.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		
		return slow;
	}
	
	public static void main(String[] args) {
		Integer[][] input = {{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5, 6}, {3, 2, 1}, {10}, {1, 2}};
        
        for(int i=0; i<input.length; i++){
          System.out.print(i+1);
          LinkList<Integer> list = new LinkList<Integer>();
          list.createLinkList(input[i]);
          System.out.print(".\tInput linked list:  ");
          list.printList();
          System.out.print("\tMiddle of the linked list is:  " );
          System.out.println(getMiddleNode(list.head).data);
          System.out.println(new String(new char[100]).replace('\0', '-'));
      }
	}
}
