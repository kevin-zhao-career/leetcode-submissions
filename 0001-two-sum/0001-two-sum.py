#include <unordered_map>

using namespace std;

typedef int TargetType;
typedef int IndexType;
typedef unordered_map<TargetType, IndexType> TargetToIndexMap;

class Solution {
public:
    vector<int> twoSum(const vector<int>& numbers, int target) {
        TargetToIndexMap target_to_index_map;
        for (auto index = 0; index != numbers.size(); ++index) {
            auto number = numbers[index];
            auto target_number = target - number;
            auto found = target_to_index_map.find(target_number);
            
            if (found != target_to_index_map.end()) {
                return {found->second, index};
            }
            else {
                target_to_index_map.insert(make_pair(number, index));
            }
        }
        return {};
    }
};