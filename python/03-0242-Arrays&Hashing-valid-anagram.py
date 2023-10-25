"""
Problem Description:
Given two strings s and t, your task is to determine if string t is an anagram of string s. An anagram is a word or phrase that is formed by rearranging the letters of another word or phrase, with each letter being used only once.

Example:
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

By rearranging the letters in "anagram", we can form the word "nagaram".

Example 2:

Input: s = "rat", t = "car"
Output: false

The two words have different sets of letters, so they can't be anagrams of each other.
"""
"""
Approaches:
Using Frequency Count (as shown in the given code):

Time Complexity: O(n) - You go through each string once.
Space Complexity: O(1) - Because the English alphabet is of constant size (26 letters), the space complexity is O(1) even though we're using two dictionaries.

Sorting:

Sort both strings and then compare if they are equal.
Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) if sorting in place, otherwise O(n).

Using Collections Counter:

Python's collections library has a Counter class which can be used to achieve the frequency count more elegantly.
Time Complexity: O(n).
Space Complexity: O(1).

Follow-up:
For Unicode characters, our approach will largely remain the same, but the space complexity could grow because the character set is larger. Still, the space complexity would be O(k) where k is the number of unique characters in the strings, which is usually bounded and relatively small. Using frequency dictionaries (like in the given approach) or Python's Counter will handle Unicode characters without any changes to the code.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if lengths are different, return False immediately if they are
        if len(s) != len(t):
            return False

        # Initialize two dictionaries to store the frequency of letters
        countS, countT = {}, {}

        # Iterate through the length of the string
        for i in range(len(s)):
            # Update the frequency for each letter in string s
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            # Update the frequency for each letter in string t
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Compare if the two frequency dictionaries are identical
        return countS == countT