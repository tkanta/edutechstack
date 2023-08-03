package com.algods.pattern.twopointers.sortcolors;

enum color{
	RED(0),WHITE(1),BLUE(2);
	private int numVal;
	color(int numVal){
		this.numVal=numVal;
	}
	public int getNumVal() {
		return numVal;
	}
}


/**
 * The space complexity of the function sortColors is O(1) because it uses a constant amount of extra space. The function only uses a few integer variables (redPointer, whitePointer, bluePointer, and temp) to keep track of indices and perform swaps, which do not depend on the size of the input array.
 * The time complexity of the sortColors function is O(n), where n is the length of the colors array. This is because the function iterates through the array once, performing constant time operations for each element.
 * @author tarin
 *
 */
public class SortColors_Self {
	
	public static int[] sortColors(int[] colors) {
		
		if(colors == null || colors.length == 0) {
			return colors;
		}
		int redIndex = 0, whiteIndex = 0, blueIndex = colors.length - 1;

		for (int i = 0; i < colors.length; i++) {
			if (colors[whiteIndex] == color.RED.getNumVal()) {
				int temp = colors[redIndex];
				colors[redIndex] = colors[whiteIndex];
				colors[whiteIndex] = temp;
				++redIndex;
				++whiteIndex;
			} else if (colors[whiteIndex] == color.WHITE.getNumVal()) {
				++whiteIndex;
			} else if (colors[whiteIndex] == color.BLUE.getNumVal()) {
				int temp = colors[whiteIndex];
				colors[whiteIndex] = colors[blueIndex];
				colors[blueIndex--] = temp;
			}
		}

		return colors;
	}
}
