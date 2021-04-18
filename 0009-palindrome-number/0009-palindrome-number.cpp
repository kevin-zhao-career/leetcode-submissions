class Solution {
public:
    bool isNegative(const int number) {
        return (number < 0);
    }
    
    bool endsWithZeroAndIsNotZero(const int number) {
        return ((number % 10 == 0) && (number != 0));
    }
    
    bool isPalindrome(int number) {
        if (isNegative(number)) {
            return false;
        }
        if (endsWithZeroAndIsNotZero(number)) {
            return false;
        }
        
        int reversedNumber = 0;
        while (number > reversedNumber) {
            reversedNumber = (reversedNumber * 10) + (number % 10);
            number /= 10;
        }
        
        return ((number == reversedNumber) || (number == (reversedNumber/10)));
    }
};