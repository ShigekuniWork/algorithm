from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # The brute force approach compares all pairs to find a valid solution.
        # However, this approach is inefficient, because it has O(N squared) time complexity.
        # I will use a hashmap to solve this problem more efficiently.
        # This approach stores previously seen numbers with their indices.
        # We iterate through the list and check whether the complement 
        # (the difference between the target and the current number) is already in the hashmap.
        # This approach achieves O(N) time and O(N) space complexity.
        
        # Initialize an empty hashmap to store numbers and their indices.
        cache = dict()
        
        # Iterate through the list with both index and value.
        for i, v in enumerate(nums):
            # Compute the complement as the difference between the target and the current number.
            complement = target - v
            # Check whether the complement is in the hashmap.
            if complement in cache:
                # If so, return the two corresponding indices.
                return [cache[complement], i]
            # Otherwise, store the current number and its index in the hashmap.
            cache[v] = i
        
        # If no valid pair is found, return an empty list.
        return []
