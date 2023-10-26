"""
Problem Description:
Given an array `nums`, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position, return the maximum number in the sliding window.

Approach:
1. Use a deque `q` to store indices of the elements, where each element in the deque represents the maximum value's index of a window.
2. As we iterate, we remove the indices of smaller values than the current value, ensuring that the front of the deque always has the maximum value of the current window.
3. When moving the window, if the left value of the window exceeds the front of the deque, we remove it from the front.
4. If the window size is reached, we add the front of the deque (max value's index) to the output.
"""

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()  # index
        l = r = 0
        
        while r < len(nums):
            # Remove indices of smaller values from the back of q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # Remove the front of the deque if it is out of the current window
            if l > q[0]:
                q.popleft()

            # If window size is reached, add the front of the deque (max value's index) to the output
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output

# Time Complexity:
# O(n), where n is the number of elements in nums. Each element is processed once.

# Space Complexity:
# O(k), where k is the size of the window. In the worst case, the deque can have k elements.
