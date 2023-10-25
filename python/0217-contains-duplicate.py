class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set. Sets store unique values.
        hashset = set()

        # Iterate over each number in the nums list
        for n in nums:
            # If the number is already in the set, it's a duplicate
            if n in hashset:
                return True
            # Otherwise, add the number to the set
            hashset.add(n)

        # If loop completes without returning, it means there's no duplicate
        return False

"""
Approaches:
Using HashSet (as shown in the given code):

Time Complexity: O(n) - You go through the list once.
Space Complexity: O(n) - In the worst case, the set can grow up to the size of the list if all numbers are distinct.
Sorting the List:

You can sort the list first and then check if any adjacent elements are the same.
Time Complexity: O(n log n) due to sorting.
Space Complexity: O(1) if you sort the list in place, otherwise O(n).
Using List's in-built functions:

You can use Python's count() function for each number but this is very inefficient.
Time Complexity: O(n^2) - For each number, you potentially go through the list.
Space Complexity: O(1).
Out of these, the given approach using HashSet is the most efficient for this problem.
"""