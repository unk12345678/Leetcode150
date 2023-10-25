"""
Problem Description:
Given an array of integers height, where each element represents a vertical line positioned at that index. 
The width of each line is 1. Find two lines, which, when combined with the x-axis, form a container that holds the most water.

Approach:
1. Initialize two pointers, one at the beginning and the other at the end of the array.
2. Calculate the area formed by the two lines at these pointers and update the maximum area if required.
3. Move the pointer pointing to the shorter line since moving the taller line inward wouldn't lead to a larger area.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1  # Initialize pointers at the two ends of the list
        res = 0  # To store the maximum area

        while l < r:
            # Calculate the area formed by the lines at the current pointers
            # The height is the minimum of the two lines and the width is the difference of their indices
            res = max(res, min(height[l], height[r]) * (r - l))
            
            # If the line at the left pointer is shorter, move the left pointer right
            if height[l] < height[r]:
                l += 1
            # Otherwise, move the right pointer left
            elif height[r] <= height[l]:
                r -= 1
                
        return res  # Return the maximum area

# Time Complexity:
# O(n), where n is the length of the height list. 
# In the worst case, we might have to move both pointers from one end of the list to the other.

# Space Complexity:
# O(1), constant space is used as we only utilize pointers and a few variables.

