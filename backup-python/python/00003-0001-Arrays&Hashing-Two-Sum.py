"""
Problem Description:
You're given an array of integers nums and an integer target. 
The task is to find two distinct indices i and j such that nums[i] + nums[j] = target and return these indices. 
It's given that there is exactly one valid answer.
"""

"""
Approaches:
Using a HashMap (as shown in the given code):

For every number n in nums, calculate the difference diff = target - n.
Check if diff exists in the map (which means we've seen a number in the array that can be added to n to give target).
Time Complexity: O(n) - We go through the list once.
Space Complexity: O(n) - In the worst case, we'll store every number from the list in the dictionary.

Brute Force:

For every number n1 in nums, iterate through the rest of the numbers in nums and check if any of them, say n2, satisfies the condition n1 + n2 = target.
Time Complexity: O(n^2) - For each number, you're potentially going through the rest of the list.
Space Complexity: O(1).

Using Sorting:

Sort the list and use two pointers technique.
Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) if sorting in place, otherwise O(n).
Given the constraints and the follow-up question, the approach using a HashMap (as shown in the provided code) is the most efficient and the preferred one.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary to store previously visited numbers and their indices
        prevMap = {}  # val -> index

        # Enumerate over the numbers to get both value and index
        for i, n in enumerate(nums):
            # Calculate the number that would sum up with 'n' to give 'target'
            diff = target - n
            
            # If this number is in our dictionary, we found a pair
            if diff in prevMap:
                return [prevMap[diff], i]
            
            # Otherwise, store the current number and its index in the dictionary
            prevMap[n] = i