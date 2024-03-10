package com.algods.pattern.binarysearch;

import java.util.Arrays;

/**
 * Time complexity O(log n), where n is number of element in array
 * Space Complexity O(1)
 * @author tarin
 *
 */
public class BinarySearch {
	
	//Own Version
//	public static int binarySearch(int[] nums, int target) {
//		
//		int startIndex = 0;
//		int endIndex = nums.length-1;
//		
//		while(startIndex <= endIndex) {
//			int midIndex = (startIndex + endIndex)/2;
//			
//			if(target == nums[midIndex]) {
//				return midIndex;
//			}else if(target > nums[midIndex]) {
//				startIndex = midIndex + 1;
//			}else {
//				endIndex = midIndex - 1;
//			}
//		}
//		
//		return -1;
//	}
	
	//Educative version
	public static int binarySearch(int[] nums, int target) {
        int low = 0;
        int high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                return mid;
            }
            else if (target < nums[mid]) {
                high = mid - 1;
            }
            else if (target > nums[mid]) {
                low = mid + 1;
            }
        }

        return -1;
    }

	
	public static void main(String[] args) {
		//https://sentry.io/answers/java-initialize-array/
		//int[] nums = new int[] {2,3,4,5,6};
//		int[] nums =  {2,3,4,5,6};
//		int[] nums_1 =  {2,3,4,5,6,8};
//		int[] nums_2 =  {-2,3,4,5,6,8};
//		int[] nums_3 =  {11, 22, 33, 44, 55, 66, 77};
//		int target = 33;
//		System.out.println(binarySearch(nums_3, target));
		//------------------
		 int[][] numsLists = {
	                {},
	                {0, 1},
	                {1, 2, 3},
	                {-1, 0, 3, 5, 9, 12},
	                {-100, -67, -55, -50, -49, -40, -33, -22, -10, -5}
	        };

	        int[] targetList = {12, 1, 3, 9, -22};
	        
	        for (int i = 0; i < numsLists.length; i++) {
	            int[] nums = numsLists[i];
	            int target = targetList[i];
	            int index = binarySearch(nums, target);
	            System.out.println((i + 1) + ".\tArray to search: " + Arrays.toString(nums));
	            System.out.println("\tTarget: " + target);
	            if (index != -1) {
	                System.out.println("\t" + target + " exists in the array at index " + index);
	            } else {
	                System.out.println("\t" + target + " does not exist in the array, so the return value is " + index);
	            }
	            System.out.println(new String(new char[100]).replace('\0', '-'));
	        }
	}
}
