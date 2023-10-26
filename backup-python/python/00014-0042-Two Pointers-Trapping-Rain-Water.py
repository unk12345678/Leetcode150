"""
Problem Description:
Given an array of non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Approach:
1. Use two pointers, one starting from the beginning and the other from the end of the array.
2. Keep track of the maximum height from the start to left pointer and from the end to right pointer.
3. The amount of water trapped at any position is the minimum of the two maximums minus the height at that position.
4. Move the pointer which has the smaller height at its current position.
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # If the height list is empty, it can't trap any water
        if not height:
            return 0

        # Initialize pointers at the two ends of the list
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]  # Initialize the maximums with the first and last elements
        res = 0  # To store the trapped water

        while l < r:
            # If the height at left pointer is less than height at right pointer
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])  # Update the leftMax
                res += leftMax - height[l]  # Add trapped water at position l
            else:
                r -= 1
                rightMax = max(rightMax, height[r])  # Update the rightMax
                res += rightMax - height[r]  # Add trapped water at position r

        return res  # Return the trapped water

# Time Complexity:
# O(n), where n is the length of the height list. 
# We move the left and right pointers from the two ends to the center.

# Space Complexity:
# O(1), constant space is used since only pointers and a few variables are utilized.

