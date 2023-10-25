"""
Problem Description:
Given a sorted array, find two numbers that add up to a specific target number. The indices should be returned in 1-based format, and it's guaranteed to have exactly one solution.

Approach:
Use a two-pointer approach with one pointer starting at the beginning and the other at the end of the array. Move the pointers towards each other based on the current sum relative to the target.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize two pointers at the start and end of the array.

        # Continue the loop until the two pointers meet
        while l < r:
            curSum = numbers[l] + numbers[r]  # Calculate the current sum of the elements at the two pointers.

            # If the current sum is greater than the target, move the right pointer leftwards
            if curSum > target:
                r -= 1
            # If the current sum is lesser than the target, move the left pointer rightwards
            elif curSum < target:
                l += 1
            # If the current sum is equal to the target, we found our pair of numbers
            else:
                return [l + 1, r + 1]  # Return the 1-based indices of the two numbers.

# Time Complexity: 
# O(n), where n is the length of numbers.
# In the worst case, we'll move both pointers from the two ends of the array to the middle.

# Space Complexity: 
# O(1), constant space, as we're using two pointers and a few variables.

