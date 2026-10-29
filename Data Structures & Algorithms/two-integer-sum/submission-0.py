class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 1

        for i in range(len(nums)):
            number = nums[i]
            complement = target - nums[i]
            
            for j in range((i+1), len(nums)):
                if complement == nums[j]:
                    return [i, j]
            
        