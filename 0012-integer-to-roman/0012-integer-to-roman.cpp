#include <string>
#include <vector>

using namespace std;

typedef vector<string> StringVector;

class Solution {
public:
    const StringVector thousands = {"", "M", "MM", "MMM"};
    const StringVector hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"}; 
    const StringVector tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    const StringVector ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    
    string intToRoman(const int number) { 
        return thousands[number / 1000] + hundreds[number % 1000 / 100] + tens[number % 100 / 10] + ones[number % 10];
    }
};