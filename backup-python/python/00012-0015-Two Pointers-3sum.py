"""
Problem Description:
Given an array of integers, find all unique triplets that sum up to zero. The solution set must not contain duplicate triplets.

Approach:
1. First, sort the numbers.
2. Use a for-loop to iterate through the numbers. For each number, employ the two-pointer technique to find pairs that sum up to the negative of that number.
3. Skip duplicates to avoid repeating triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # List to store the result triplets
        nums.sort()  # Sort the input list

        for i, a in enumerate(nums):
            # Skip positive integers since they can't sum to a negative value to give zero
            if a > 0:
                break

            # Skip duplicates to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Initialize two pointers, one just after the current number and the other at the end of the list
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                # If the sum of the triplet is greater than zero, move the right pointer left
                if threeSum > 0:
                    r -= 1
                # If the sum of the triplet is less than zero, move the left pointer right
                elif threeSum < 0:
                    l += 1
                else:  # A triplet is found
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates with the left pointer
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res

# Time Complexity:
# O(n^2), where n is the length of nums. 
# For each element in nums, we might have to move the two pointers from one end to the other.

# Space Complexity:
# O(1), if we don't count the space needed for the output. Otherwise, O(n) in the worst case.

