class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = set(range(len(nums)+1))
        actual = {num for num in nums}

        difference = list((expected.difference(actual)))

        return difference.pop()