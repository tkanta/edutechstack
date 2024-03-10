package com.algods.pattern.binarysearch;

import java.util.Arrays;
import java.util.List;

public class BinarySearchRotated {
	
	/**
	 * Own version not completed
	 * @param nums
	 * @param target
	 * @return
	 */
//	public static int binarySearchRotated(List<Integer> nums, int target) {
//		
//		int startIndex = 0;
//		int endIndex = nums.size()-1;
//		int midIndex = 0;
//		
//		while(startIndex <= endIndex) {
//			midIndex = (startIndex + endIndex)/2;
//			
//			if(nums.get(midIndex).equals(target)) {
//				return midIndex;
//			}else if( (target > nums.get(midIndex) && target <= nums.get(endIndex)) ||
//					(target < nums.get(midIndex) && target < nums.get(startIndex)) ) {
//				startIndex = midIndex + 1;
//			}else if ( (target < nums.get(midIndex) && target > nums.get(startIndex)) ||
//					(target > nums.get(midIndex) && target > nums.get(startIndex)) ) {
//				endIndex = midIndex - 1;
//			}
//			
//		}
//		return -1;
//	}
	
	public static int binarySearchRotated(List<Integer> nums, int target) {
		
		int start = 0;
		int end = nums.size() - 1 ; 
		
		while(start <= end) {
			int mid = start + (end - start)/2;
			
			if(nums.get(mid) == target) {
				return mid;
			}
			
			// when start to mid is sorted
			if(nums.get(start) <= nums.get(mid)) {
				if(target >= nums.get(start) && target <= nums.get(mid)) {
					end = mid - 1;
				}else {
					start = mid + 1;
				}
			}else { // when mid to end is sorted
				if(target >= nums.get(mid) && target <= nums.get(end)) {
					start = mid + 1; 
				}else {
					end = mid - 1 ;
				}
			}
			
		}
		
		return -1;
	}
	public static void main(String[] args) {
		
		
//		List<Integer> nums_3 = Arrays.asList(55, 66, 77, 11, 22, 33, 44);
//		int target = 66;
//		List<Integer> nums_3 = Arrays.asList(4, 5, 6, 1, 2, 3);
//		int target = 3;
//		System.out.println(binarySearchRotated(nums_3, target));
		
		//-----------------
		
		List<List<Integer>> numList = Arrays.asList(
	            Arrays.asList(5, 6, 7, 1, 2, 3, 4),
	            Arrays.asList(40, 50, 60, 10, 20, 30),
	            Arrays.asList(47, 58, 69, 72, 83, 94, 12, 24, 35),
	            Arrays.asList(77, 82, 99, 105, 5, 13, 28, 41, 56, 63),
	            Arrays.asList(48, 52, 57, 62, 68, 72, 5, 7, 12, 17, 21, 28, 33, 37, 41)
	        );

	        List<Integer> targetList = Arrays.asList(1, 50, 12, 56, 5);

	        for (int i = 0; i < targetList.size(); i++) {
	            System.out.println((i + 1) + ".\tSorted array: " + numList.get(i) +
	                "\n\ttarget " + targetList.get(i) +
	                " found at index " + binarySearchRotated(numList.get(i), targetList.get(i)));
	            System.out.println(new String(new char[100]).replace('\0', '-'));
	        }
	}
	
}
