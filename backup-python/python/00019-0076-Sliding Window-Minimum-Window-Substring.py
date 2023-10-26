"""
Problem Description:
Given two strings `s` and `t`, return the minimum window in `s` which will contain all the characters in `t`.

Approach:
1. Use `countT` dictionary to maintain the frequency count of characters in `t`.
2. Use `window` dictionary to maintain the frequency count of characters in the current window of `s`.
3. `have` keeps track of characters of `t` currently satisfied by the window, while `need` is the total characters we need to satisfy.
4. If a character in the window matches the count required from `t`, increment `have`.
5. If all characters of `t` are satisfied (i.e., `have == need`), try to shrink the window from the left to find the minimum window that still satisfies `t`.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                # Update our result if current window is smaller than previously found
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # Move the left pointer to shrink the window
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if resLen != float("infinity") else ""

# Time Complexity:
# O(n), where n is the length of string s. In the worst case, each character in s is processed twice (once by the right pointer and once by the left pointer).

# Space Complexity:
# O(k), where k is the number of unique characters in t. In the worst case, the space used by countT and window dictionaries combined is 2k.
