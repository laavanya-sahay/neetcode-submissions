class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for num in range(n + 1):
            bits = 0
            while num != 0:
                bits += num % 2
                num = num // 2
            result += [bits]
        return result