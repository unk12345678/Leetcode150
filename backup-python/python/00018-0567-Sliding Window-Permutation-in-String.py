"""
Problem Description:
Determine if some permutation of string `s1` is a substring of string `s2`. Essentially, we need to find if a string exists in `s2` such that it is an anagram of `s1`.

Approach:
1. Create two frequency count arrays, `s1Count` and `s2Count`, for `s1` and `s2` respectively. 
2. Initially, fill the count arrays based on the first `len(s1)` characters of both strings.
3. Use a sliding window of size `len(s1)` to iterate over `s2` and update the `s2Count` array accordingly.
4. At each step, check if the count arrays are the same, indicating a match. If a match is found, return True.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26

        # Initialize frequency count arrays for s1 and the first len(s1) characters of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord("a")] += 1
            s2Count[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            matches += 1 if s1Count[i] == s2Count[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # Slide the window over s2
            index = ord(s2[r]) - ord("a")
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            # Remove the leftmost character from the window
            index = ord(s2[l]) - ord("a")
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        return matches == 26

# Time Complexity:
# O(n), where n is the length of string s2. Each character in s2 is processed once.

# Space Complexity:
# O(1), constant space used for the `s1Count` and `s2Count` arrays.
