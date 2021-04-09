#include <vector>

using namespace std;

typedef vector<int> Numbers;

class Solution {
public:
    vector<int> runningSum(Numbers & numbers) {
        for (auto index = 1; index != numbers.size(); ++index) {
            numbers[index] += numbers[index - 1];
        }
        return numbers;
    }
};