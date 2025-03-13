class Solution {
public:
    int removeDuplicates(vector<int>& numbers) {
        return distance(begin(numbers), unique(begin(numbers), end(numbers)));
    }
};
