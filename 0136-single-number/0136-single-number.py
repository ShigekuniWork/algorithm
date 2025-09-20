class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # We solve this with XOR to meet O(n) time and O(1) space.
        # When a number appears twice, XOR makes it zero.
        # And when we XOR with zero, we just get the number back.
        # So, after going through the list, only the single number stays.

        # Start with zero.
        result = 0

        # The loop XORs each number with result.
        for n in nums:
            # After XOR, duplicates cancel out.
            result ^= n

        # At the end, result is the single number.
        return result

        # Time is O(n). Space is O(1).
