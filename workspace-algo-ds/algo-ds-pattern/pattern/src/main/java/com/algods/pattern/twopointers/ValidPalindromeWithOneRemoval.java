package com.algods.pattern.twopointers;

public class ValidPalindromeWithOneRemoval {

	private static boolean isPalindrome(String s) {
		
		int left = 0;
		int right = s.length() - 1;
		
		int skip = 0;
		
		while(left < right) {
			if(s.charAt(left) == s.charAt(right)) {
				left++;
				right--;
				continue;
			}else if(s.charAt(left) != s.charAt(right) && skip < 1) {
				if(s.charAt(left+1) == s.charAt(right)) {
					left++;
				}else if(s.charAt(left) == s.charAt(right-1)) {
					right--;
				}
				skip++;
				continue;
			}else {
				return false;
			}
		}
		
		
		return true;
	}
	
	public static void main(String[] args) {
		String[] strs = new String[] { "abceba", "raceacat", "deead","madame", "dead", "abca", "tebbem", "eeccccbebaeeabebccceea",
				"ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno" };
		for(String s : strs) {
			System.out.println(s + " is palindrom ? "+ isPalindrome(s));
		}
	}
}
