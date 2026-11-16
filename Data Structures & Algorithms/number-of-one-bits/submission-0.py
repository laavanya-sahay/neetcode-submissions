class Solution:
    def hammingWeight(self, n: int) -> int:
        bits_so_far = 0

        while n != 0:
            bits_so_far += n % 2
            n = n // 2
        
        return bits_so_far
