class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        sorted_nums = sorted(freq, key=lambda n: freq[n], reverse = True)
        return sorted_nums[:k]