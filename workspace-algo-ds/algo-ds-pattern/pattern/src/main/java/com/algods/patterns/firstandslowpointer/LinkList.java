package com.algods.patterns.firstandslowpointer;

public class LinkList<T> {
	
	public LinkListNode<T> head;
	public LinkListNode<T> tail;
	
	public void insertNodeAtHead(LinkListNode<T> node) {
		if(this.head == null) {
			this.head = node;
			this.tail = node;
		}else {
			node.next = this.head;
			this.head = node;
		}
	}
	
	public void createLinkList(T[] list) {
		for(int i=list.length-1; i >= 0; i--) {
			
			LinkListNode<T> node = new LinkListNode<T>(list[i]);
			insertNodeAtHead(node);
		}
		//		for(T i: list) {
		//			LinkListCycleNode<T> node = new LinkListCycleNode<T>(i);
		//			insertNodeAtHead(node);
		//		}
	}
	
	public void printList() {
		LinkListNode<T> temp = this.head;
		
		while(temp != null) {
			System.out.print(temp.data);
			temp = temp.next;
			if(temp != null) {
				System.out.print(" -> ");
			}else {
				System.out.print(" -> Null ");
			}
		}
	}
	
	/**
	 * create cycle by pointing the tail to the node at position
	 * @param pos
	 */
	public void createCycle(int pos) {
		LinkListNode<T> ptr = this.head;
		if(pos != -1) {
			int p = 0;
			while(p < pos) {
				ptr = ptr.next;
				p++;
			}
			this.tail.next = ptr;
		}
	}
	
}
