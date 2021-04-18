#include <unordered_map>

class Solution {
public:
    const unordered_map<string, int> ROMAN_NUMBERAL_TO_NUMBER_MAP = {
        {"I", 1},
        {"V", 5},
        {"X", 10},
        {"L", 50},
        {"C", 100},
        {"D", 500},
        {"M", 1000},
        {"IV", 4},
        {"IX", 9},
        {"XL", 40},
        {"XC", 90},
        {"CD", 400},
        {"CM", 900}
    };
    
    int romanToInt(const string & roman_number_string) {
        auto last_symbol = roman_number_string.substr(roman_number_string.length() - 1, 1);
        auto find_itr = ROMAN_NUMBERAL_TO_NUMBER_MAP.find(last_symbol);
        auto last_value = (find_itr == ROMAN_NUMBERAL_TO_NUMBER_MAP.end()) ?
            0 : (find_itr->second);
        auto total = last_value;

        for (int index = roman_number_string.size() - 2; index >= 0; index--) {
            auto current_symbol = roman_number_string.substr(index, 1);
            auto find_itr = ROMAN_NUMBERAL_TO_NUMBER_MAP.find(current_symbol);
            auto current_value = (find_itr == ROMAN_NUMBERAL_TO_NUMBER_MAP.end()) ?
                0 : (find_itr->second);
            

            if (current_value < last_value) {
                total -= current_value;
            } else {
                total += current_value;
            }
            last_value = current_value;
        }
        return total;
    }
};