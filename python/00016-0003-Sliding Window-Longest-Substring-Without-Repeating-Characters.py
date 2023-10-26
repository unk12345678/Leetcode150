"""
Problem Description:
Given a string, find the length of the longest substring without repeating characters.

Approach:
1. Utilize a sliding window approach.
2. Use a set to keep track of characters in the current substring.
3. If a character is repeated, move the left pointer of the window to the right.
4. Calculate the maximum length of the substring without repeating characters during each iteration.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()  # Set to store characters of current substring
        l = 0  # Left pointer of the sliding window
        res = 0  # Result to store the maximum length of substring

        # Iterate through the string with the right pointer
        for r in range(len(s)):
            # If the character is in the set, remove the leftmost character and move the left pointer
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            # Add the current character to the set
            charSet.add(s[r])
            # Update the result with the new length of the substring
            res = max(res, r - l + 1)

        return res  # Return the maximum length

# Time Complexity:
# O(n), where n is the length of string s.
# In the worst case, each character will be visited twice (once by r pointer and once by l pointer).

# Space Complexity:
# O(min(n, m)), where n is the length of string s and m is the size of the charset/alphabet.
# The size of the set can grow up to the size of the charset in the worst case.

