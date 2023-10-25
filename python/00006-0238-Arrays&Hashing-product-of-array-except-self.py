"""
Problem Description:
You're given an array of integers, nums. Your task is to produce a new array where each index i in the new array contains the product of all numbers in nums except nums[i]. You're not allowed to use division and the solution must run in O(n) time.

Example:
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Explanation of the Current Code:
The current code approach is to use two iterations:

First iteration populates the res list with prefix products.
Second iteration modifies the res list by multiplying each entry with the corresponding postfix product.
"""
"""
Approaches:

Using Prefix and Postfix Products (as shown in the given code):

Calculate the prefix products and store them in res.
Use a variable postfix to keep track of the postfix product as you iterate from the end to the start of nums. Multiply each entry in res with postfix.
Time Complexity: O(n).
Space Complexity: O(1) - This doesn't include the space used by the output.

Using Two Separate Arrays for Prefix and Postfix Products:

Calculate prefix and postfix products using two separate arrays.
For each index i, the product of all numbers except nums[i] would be prefix[i] * postfix[i].
Time Complexity: O(n).
Space Complexity: O(n) - This includes space used by prefix and postfix arrays but excludes the space used by the output.
The given solution using the prefix and postfix products approach with a single iteration for each is efficient and answers the problem's requirements effectively. It achieves the goal with O(1) extra space, as the output space does not count towards the space complexity analysis.
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize result array with all 1's.
        res = [1] * (len(nums))

        # Populate res with prefix products.
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]

        # Multiply each entry of res with the corresponding postfix product.
        postfix = 1  # Start with 1 for the very last element.
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
