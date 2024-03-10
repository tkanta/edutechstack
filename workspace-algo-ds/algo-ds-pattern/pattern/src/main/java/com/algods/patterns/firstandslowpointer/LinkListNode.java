package com.algods.patterns.firstandslowpointer;

public class LinkListNode<T> {
	
	public T data;
	public LinkListNode<T> next;
	
	public LinkListNode(T data) {
		this.data = data;
		this.next = null;
	}

}
