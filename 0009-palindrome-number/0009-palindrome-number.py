class Solution:
    def isPalindrome(self, number: int) -> bool:
        return (str(number) == str(number)[::-1])