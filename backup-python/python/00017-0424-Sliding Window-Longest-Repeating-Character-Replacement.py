"""
Problem Description:
Given a string `s` and an integer `k`, the goal is to replace any character in the string such that the resulting string has the longest repeating character. Return the length of this substring.

Approach:
1. Use a sliding window to maintain a segment of the string.
2. Keep track of the frequency of each character within the window using a dictionary `count`.
3. At every step, calculate the character with the maximum frequency (`maxf`) within the window.
4. If the window's size minus `maxf` is greater than `k` (i.e., the number of replacements needed is more than `k`), then slide the window.
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # Dictionary to store frequency of each character in the current window
        
        l = 0  # Left pointer for sliding window
        maxf = 0  # Variable to store the maximum frequency character in the window
        
        # Right pointer to iterate over the string
        for r in range(len(s)):
            # Update the count of the current character
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Update maxf with the maximum frequency character seen so far
            maxf = max(maxf, count[s[r]])

            # If replacements needed exceed k, slide the window
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1  # Decrease the count of the leftmost character
                l += 1  # Slide the window

        return (r - l + 1)  # Return the size of the window

# Time Complexity:
# O(n), where n is the length of string s. 
# The window slides over the string with each character being processed once.

# Space Complexity:
# O(26) = O(1), constant space for the `count` dictionary as there are 26 English letters.
