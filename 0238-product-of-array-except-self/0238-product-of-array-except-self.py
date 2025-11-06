class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        I'd approach to solve this problem by using prefix and suffix products.
        First, iterate through nums and multiply the prefix (product of all previous elements) 
        to each position in the response.
        Then iterate through the reversed list and multiply the suffix (product of all following elements)
        to each position in the response.
        """
        # Assign one to the list value
        response = [1] * len(nums)

        # Loop start, i over index of nums
        prefix = 1
        for i in range(len(nums)):
            # Multiply prefix to response
            response[i] *= prefix
            # Update prefix as the result of multiplying prefix and num
            prefix *= nums[i]

        # Suffix loop start as well from end to first
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            response[i] *= suffix
            suffix *= nums[i]
        
        # Return list that contains products of array except self
        return response

        """
        Time complexity is O(N)
        Space complexity is O(1)
        """