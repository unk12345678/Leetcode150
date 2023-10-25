"""
Problem Description:
You're given an array of integers, nums, and an integer, k. 
Your task is to determine the k most frequent elements from nums.
"""
"""
Approaches:
Using Frequency Lists (as shown in the given code):

Count the occurrences of each number and store them in a dictionary (count).
Use another list (freq) where the ith index contains a list of numbers with a frequency of i.
Time Complexity: O(n) - We only iterate through the list of numbers and their unique counts.
Space Complexity: O(n).
Using Min-Heap:

Count the occurrences of each number.
Add the numbers and their frequencies to a min-heap until there are k items in the heap. If there are more than k items, remove the smallest one.
Time Complexity: O(n + k log n) - Counting occurrences takes O(n), and constructing the heap takes O(k log n).
Space Complexity: O(n).
Using Bucket Sort:

Similar to the frequency list approach, but instead of a list of lists, use a list of sets.
Time Complexity: O(n).
Space Complexity: O(n).
The given solution using the frequency list approach is efficient for this problem given the constraints. The solution effectively groups numbers by their frequencies and returns the top k frequent numbers. The code also adheres to the follow-up condition of having a time complexity better than O(n log n).
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each number.
        count = {}
        
        # List of lists to store numbers that have a specific frequency.
        freq = [[] for i in range(len(nums) + 1)]

        # Counting occurrences of each number.
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Storing numbers in the freq list based on their frequencies.
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Iterating over the freq list from the end to the beginning (high frequency to low frequency).
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
