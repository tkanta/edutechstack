package com.algods.pattern.twopointers;

public class ReverseWords {

	private static String reverseWords_self(String str) {
		String[] strArr = str.split("\\s+");
		
		StringBuilder sb = new StringBuilder();
		for(int i=strArr.length-1; i >= 0 ; i-- ) {
			sb.append(strArr[i]);
			sb.append(" ");
		}
		return sb.toString();
	}
	
//	public static void main(String[] args) {
//		String str = "Tarini Kanta Negi";
//		System.out.println(reverseWords_self(str));
//	}
	
	public static void main(String[] args) {
		String[] inputs = { "Hello World!", "We love Python.", "The quick brown fox jumped over the lazy dog.", "Hey!",
				"To be, or not to be", "AAAAA", "Hello     World" };
		for (int i = 0; i < inputs.length; i++) {
			System.out.print(i + 1);
			System.out.println(".\tActual string:\t\t" + inputs[i]);
			System.out.println("\tReversed String:\t" + reverseWords_self(inputs[i]));
			System.out.println("--------------------------------------------");
		}

	}
}
