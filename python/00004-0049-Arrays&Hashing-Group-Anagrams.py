"""
Problem Description:
You're given an array of strings, strs. Your task is to group the anagrams together. An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example:
Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

"""
Approaches:
Using Character Counts (as shown in the given code):

Use a hash map with a key as the character count of a word and the value as a list of words that have that character count.
Time Complexity: O(n * k) where n is the number of words and k is the maximum length of a word.
Space Complexity: O(n * k).
Using Sorted Words:

Instead of using character counts, you can sort each word and use the sorted word as a key in a hash map.
Time Complexity: O(n * k log k) due to sorting.
Space Complexity: O(n * k).
Given the constraints, the character count approach (as shown in the provided code) is more efficient in terms of time complexity than the sorted words approach. The logic is neat, and the use of a defaultdict makes handling lists for each unique key more convenient.
"""
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Using a defaultdict where each key is a tuple of 26 integers representing 
        # the character count and each value is a list of words (anagrams) with that character count.
        ans = collections.defaultdict(list)

        # For every word in the list
        for s in strs:
            # Initialize a list of 26 zeros for the English alphabet.
            count = [0] * 26
            # For every character in the word, increment the count for that character.
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            # The count list is converted to a tuple (because lists can't be used as dictionary keys)
            # and used as a key in the defaultdict. The word is then appended to the list corresponding to that key.
            ans[tuple(count)].append(s)
        
        # Return the grouped anagrams as lists.
        return ans.values()
