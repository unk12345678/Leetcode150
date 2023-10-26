"""
Problem Description:
The task is to determine if a given string is a palindrome considering only alphanumeric characters and ignoring spaces or any other special characters. 
Palindrome means the string reads the same backward as forward.
"""
"""
The approach is straightforward: use two pointers to traverse the string from the two ends and compare the characters. If all the alphanumeric characters match from both ends till the pointers meet, the string is a palindrome. 
The alphanum helper function checks if a character is alphanumeric.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize pointers for two ends of the string

        # Loop until left pointer is less than right pointer
        while l < r:
            # Increment the left pointer if the current character is not alphanumeric
            while l < r and not self.alphanum(s[l]):
                l += 1
            # Decrement the right pointer if the current character is not alphanumeric
            while l < r and not self.alphanum(s[r]):
                r -= 1
            # If alphanumeric characters from the front and back don't match, it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            # Move both pointers inward for next comparison
            l += 1
            r -= 1
        # If loop completes without returning False, it's a palindrome
        return True

    # Helper function to check if character is alphanumeric
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )

# Time Complexity: 
# O(n), where n is the length of string s.
# Each character in s is examined once.

# Space Complexity: 
# O(1), constant space as only two pointers and a few variables are used.
