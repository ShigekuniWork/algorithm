class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_length = len(nums)
        expected_sum = expected_length * (expected_length + 1) // 2
        actal_sum = sum(nums)

        return expected_sum - actal_sum
