#include <algorithm>
#include <vector>

using namespace std;

/**
 * Name: Kevin Zhao
 * Runtime Complexity: O(log n)
 * Space Complexity: O(1)
 */

class Solution {
public:
    vector<int> searchRange(vector<int>& numbers, int target) {
        if (numbers.empty()) {
            return {-1, -1};
        }
        
        auto iterator_range = equal_range(numbers.begin(),
                                          numbers.end(),
                                          target);
        auto begin_index = static_cast<int>(iterator_range.first - numbers.begin());
        auto end_index = static_cast<int>(iterator_range.second - numbers.begin()) - 1;
        
        begin_index = ((begin_index != numbers.size()) && (numbers[begin_index] == target)) ?
            (begin_index) : (-1);
        end_index = ((end_index != -1) && (numbers[end_index ] == target)) ?
            (end_index) : (-1);

        return {begin_index, end_index};
    }
};