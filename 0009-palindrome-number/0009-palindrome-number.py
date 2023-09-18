class Solution:
    def isPalindrome(self, integer: int) -> bool:
        if integer < 0 or (integer != 0 and integer % 10 == 0):
            return False

        reversed_num = 0
        original = integer

        while integer > reversed_num:
            reversed_num = reversed_num * 10 + integer% 10
            integer //= 10

        return integer == reversed_num or integer == reversed_num // 10
