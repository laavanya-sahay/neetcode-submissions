class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = {num for num in nums}
        return len(nums) != len(nums_set)
        