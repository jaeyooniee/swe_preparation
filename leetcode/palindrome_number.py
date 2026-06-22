class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        n = x
        m = 0
        mult = 0

        while n != 0:
            m = m*10 + n%10
            n //= 10

        return x == m