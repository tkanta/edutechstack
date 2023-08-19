package com.algods.patterns.firstandslowpointer;

public class FindHappyNumber_self {
	
	
	public static int sumOfSquaredDigits(int number) {
	      int totalSum = 0;
	      while (number != 0) {
	        int digit = number % 10;
	        number = number / 10;
	        totalSum += (Math.pow(digit, 2));
	      }
	      return totalSum;
	  }
	
	public static boolean isHappyNumber(int number) {
		
		int slow = number;
		int fast = sumOfSquaredDigits(number);
		
		while(fast != 1 && fast != slow) {
			slow = sumOfSquaredDigits(slow);
			fast = sumOfSquaredDigits(sumOfSquaredDigits(fast));
		}
		
		return fast == 1;
	}
	
	public static void main(String[] args) {
		System.out.println(isHappyNumber(2));
//		System.out.println(2345/10);
//		System.out.println(2345%10);
	}
}
