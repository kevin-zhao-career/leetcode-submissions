#include <string>
#include <vector>

using namespace std;

class Solution {
public:
   string get_range(const vector<int>& nums, int start_range_index, int index) {
        string range;
        range += to_string(nums[start_range_index]);
        if (index - start_range_index > 1) {
            range += "->";
            range += to_string(nums[index - 1]);
        }
        return range;
    }

    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.empty()) {
            return {};
        }
        vector<string> ranges;
        ranges.reserve(nums.size());
        int start_range_index = 0;
        long last_num = nums.front();
        int i = 1;
        while (i < nums.size()) {
            const long diff = nums[i] - last_num; // avoiding integer overflow
            if (diff > 1) {
                ranges.push_back(get_range(nums, start_range_index, i));
                start_range_index = i;
            }
            last_num = nums[i++];
        }
        ranges.push_back(get_range(nums, start_range_index, i));
        return ranges;
    }
};