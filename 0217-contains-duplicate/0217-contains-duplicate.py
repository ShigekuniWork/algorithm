class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        origin_total = len(nums)
        set_total = len(set(nums))

        return origin_total != set_total
        