class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_str = ""

        while n != 0:
            reverse_str += str(n % 2)
            n = n // 2
        
        reverse_str += "0" * (32-len(reverse_str))
        
        sum_so_far = 0
        for bit in range(-1, -33, -1):
            if int(reverse_str[bit]) == 1:
                sum_so_far += 2**(-bit-1)
        
        return sum_so_far