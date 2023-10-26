"""
Problem Description:
The goal is to determine the length of the longest consecutive elements subsequence from a given list of integers.
"""
"""
The main idea of this solution is to iterate through the set of numbers, and for each number that could potentially be the start of a new sequence, it tries to find how long the sequence is by looking for consecutive numbers. 
The use of a set ensures constant time checks for the existence of numbers.
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert list to set for O(1) time complexity look-ups
        numSet = set(nums)
        longest = 0  # Variable to store the result

        for n in numSet:
            # Check if the current number 'n' is the start of a sequence.
            # A number 'n' starts a sequence if 'n-1' is not in the set.
            if (n - 1) not in numSet:
                length = 1  # Start length counter for this sequence
                # As long as the next number in the sequence is in the set, keep counting.
                while (n + length) in numSet:
                    length += 1
                # Update the longest length if the current sequence is longer.
                longest = max(length, longest)
                
        return longest

# Time Complexity: 
# O(n), where n is the number of elements in nums. 
# Although there's a while loop inside the for loop, the while loop runs for each number only once.

# Space Complexity: 
# O(n), where n is the number of elements in nums, because of the set used.
