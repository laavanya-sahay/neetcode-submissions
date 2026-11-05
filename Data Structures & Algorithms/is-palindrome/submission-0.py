class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = [ch.lower() for ch in s if ch.isalnum()]
        backward = forward.copy()

        backward.reverse()

        return forward == backward

        